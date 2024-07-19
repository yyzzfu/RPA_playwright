import hashlib
import shutil
import os
import sys
import time
import warnings
from typing import Any, Callable, Dict, Generator, List, Optional

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
)
from slugify import slugify
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    pw = sync_playwright().start()
    session_start_time = time.time()
    yield pw
    print(f"-----------本轮测试耗时{int(time.time()-session_start_time)}秒----------")
    pw.stop()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1440,
            "height": 900,
        },
        "record_video_size": {
            "width": 1440,
            "height": 900,
        }
    }


@pytest.fixture
def context(
        browser: Browser,
        browser_context_args: Dict,
        pytestconfig: Any,
        request: pytest.FixtureRequest,
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
                # allure.attach.file(screenshot_path, '最终截图', allure.attachment_type.PNG)
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
                # allure.attach.file(os.path.join(output_dir, request.node.name, file_name), "过程录像", allure.attachment_type.WEBM)
            except Error:
                # Silent catch empty videos.
                pass


@pytest.fixture()
def pw_page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page


@pytest.fixture()
def data_for_test():
    # wechat_name_list = ['fyq测试1', 'fyq测试2']
    wechat_name_list = ['fyq测试1']
    user = ('kf5', 'Qwer1234')
    yield wechat_name_list, user


@pytest.fixture(scope='session')
def global_map():
    from utils.global_map import GlobalMap
    global_map = GlobalMap()
    yield global_map
    global_map.delete_file()


@pytest.fixture()
def get_send_content_dic():
    from utils.tools import get_path, get_my, get_time_now

    def send_content_dic(described):
        time_now = get_time_now()
        mrmy = get_my()
        task_name = f'{described}{time_now}'
        send_content_dic = {"content_dic": {'text': f'{described}{time_now}(测试)' + mrmy,
                                            # 'picture': get_path(r'/upload/pciture.jpg'),
                                            # 'video': get_path(r'/upload/video.mp4'),
                                            # 'link': {'title': f'链接的标题{time_now}', 'address': r'http://www.baidu.com',
                                            #          'content': f'内容简介:{described}{time_now}',
                                            #          'picture_path': get_path(r'/upload/pciture.jpg')},
                                            # 'file': {'file_name': f'文件的名称{time_now}',
                                            #          'file_path': get_path(r'/upload/file.pdf')},
                                            # 'notice': f'{described}-群公告内容：{mrmy}{time_now}'
                                            },
                            "task_name": task_name}
        return send_content_dic
    yield send_content_dic
