import hashlib
import shutil
import os
import sys
import time
import warnings
from typing import Any, Callable, Dict, Generator, List, Optional, cast

import allure
import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    BrowserType,
    Error,
    Page,
    Playwright,
    sync_playwright,
    expect)
from pytest_playwright.pytest_playwright import CreateContextCallback
from slugify import slugify
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#
# @pytest.fixture(scope="session")
# def playwright() -> Generator[Playwright, None, None]:
#     pw = sync_playwright().start()
#     session_start_time = time.time()
#     yield pw
#     print(f"-----------本轮测试耗时{int(time.time()-session_start_time)}秒----------")
#     pw.stop()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig):
    width, height = pytestconfig.getoption("--viewport")
    return {
        **browser_context_args,
        "viewport": {
            "width": width,
            "height": height,
        },
        "record_video_size": {
            "width": width,
            "height": height,
        }
    }


def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("playwright", "Playwright")
    group.addoption(
        "--viewport",
        action="store",
        default=[1440, 900],
        help="viewport size set",
        type=int,
        nargs=2,
    )
    group.addoption(
        "--ui_timeout",
        default=30_000,
        help="locator timeout and expect timeout",
    )


@pytest.fixture(scope="session")
def ui_timeout(pytestconfig):
    timeout = float(pytestconfig.getoption("--ui_timeout"))
    expect.set_options(timeout=timeout)  # 设置断言的超时时间
    return timeout


@pytest.fixture
def context(
        browser: Browser,
        browser_context_args: Dict,
        pytestconfig: Any,
        request: pytest.FixtureRequest,
        ui_timeout
) -> Generator[BrowserContext, None, None]:
    pages: List[Page] = []

    tempdir = tempfile.gettempdir()
    output_dir = pytestconfig.getoption("--output")
    log_dir = os.path.join(output_dir, request.node.name)
    os.makedirs(log_dir, exist_ok=True)

    # video_option = pytestconfig.getoption("--video")
    # rerun_count = pytestconfig.getoption("--reruns")
    # browser_context_args["record_video_dir"] = artifacts_folder.name
    # video_on = False
    # if video_option == "on":
    #     if rerun_count:
    #         if rerun_count == request.node.execution_count:
    #             video_on = True
    #     else:
    #         video_on = True
    # elif video_option == "retain-on-failure":
    #     video_on = True
    # if not video_on:
    #     browser_context_args.pop("record_video_dir")

    context_args_marker = next(request.node.iter_markers("browser_context_args"), None)
    additional_context_args = context_args_marker.kwargs if context_args_marker else {}
    browser_context_args.update(additional_context_args)

    context = browser.new_context(**browser_context_args)
    context.set_default_timeout(ui_timeout)   # 设置超时时间
    context.set_default_navigation_timeout(ui_timeout * 2)
    context.on("page", lambda page: pages.append(page))

    tracing_option = pytestconfig.getoption("--tracing")
    capture_trace = tracing_option in ["on", "retain-on-failure"]
    if capture_trace:
        context.tracing.start(
            title=slugify(request.node.nodeid),
            screenshots=True,
            snapshots=True,
            sources=True,
        )

    yield context

    # If request.node is missing rep_call, then some error happened during execution
    # that prevented teardown, but should still be counted as a failure
    failed = request.node.rep_call.failed if hasattr(request.node, "rep_call") else True

    if capture_trace:
        retain_trace = tracing_option == "on" or (
                failed and tracing_option == "retain-on-failure"
        )
        if retain_trace:
            trace_path = os.path.join(output_dir, request.node.name, "trace.zip")
            context.tracing.stop(path=trace_path)
        else:
            context.tracing.stop()

    screenshot_option = pytestconfig.getoption("--screenshot")
    capture_screenshot = screenshot_option == "on" or (
            failed and screenshot_option == "only-on-failure"
    )
    if capture_screenshot:
        for index, page in enumerate(pages):
            human_readable_status = "failed" if failed else "finished"
            screenshot_path = os.path.join(output_dir, request.node.name, f"test-{human_readable_status}-{index+1}.png")
            try:
                page.screenshot(
                    timeout=5000,
                    path=screenshot_path,
                    full_page=pytestconfig.getoption("--full-page-screenshot"),
                )
                allure.attach.file(screenshot_path, '最终截图', allure.attachment_type.PNG)
            except Error:
                pass

    context.close()

    video_option = pytestconfig.getoption("--video")
    preserve_video = video_option == "on" or (
            failed and video_option == "retain-on-failure"
    )
    if preserve_video:
        for page in pages:
            video = page.video
            if not video:
                continue
            try:
                video_path = video.path()
                file_name = os.path.basename(video_path)
                video.save_as(
                    path=os.path.join(output_dir, request.node.name, file_name)
                )
                allure.attach.file(os.path.join(output_dir, request.node.name, file_name), "过程录像", allure.attachment_type.WEBM)
            except Error:
                # Silent catch empty videos.
                pass


@pytest.fixture()
def pw_page(context: BrowserContext):
    page = context.new_page()
    yield page


@pytest.fixture(scope='session')
def global_map():
    from utils.global_map import GlobalMap
    global_map = GlobalMap()
    yield global_map
    global_map.delete_file()


@pytest.fixture()
def get_kf(worker_id):
    user_list = ['kf2', 'kf3']
    if worker_id.startswith('gw'):
        user = user_list[int(worker_id[2:])]
    else:
        user = 'kf2'
    return user


@pytest.fixture
def new_context(
    browser: Browser,
    browser_context_args: Dict,
    _artifacts_recorder: "ArtifactsRecorder",
    request: pytest.FixtureRequest,
    ui_timeout,
) -> Generator[CreateContextCallback, None, None]:
    browser_context_args = browser_context_args.copy()
    context_args_marker = next(request.node.iter_markers("browser_context_args"), None)
    additional_context_args = context_args_marker.kwargs if context_args_marker else {}
    browser_context_args.update(additional_context_args)
    contexts: List[BrowserContext] = []

    def _new_context(**kwargs: Any) -> BrowserContext:
        context = browser.new_context(**browser_context_args, **kwargs)
        context.set_default_timeout(ui_timeout)
        context.set_default_navigation_timeout(ui_timeout * 2)
        original_close = context.close

        def _close_wrapper(*args: Any, **kwargs: Any) -> None:
            contexts.remove(context)
            _artifacts_recorder.on_will_close_browser_context(context)
            original_close(*args, **kwargs)

        context.close = _close_wrapper
        contexts.append(context)
        _artifacts_recorder.on_did_create_browser_context(context)
        return context

    yield cast(CreateContextCallback, _new_context)
    for context in contexts.copy():
        context.close()

