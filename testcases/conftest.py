import hashlib
import shutil
import os
import sys
import warnings
from typing import Any, Callable, Dict, Generator, List, Optional

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
# from slugify import slugify
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


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


@pytest.fixture()
def pw_page(context):
    page = context.new_page()
    yield page


@pytest.fixture()
def data_for_test():
    # wechat_name_list = ['fyq测试1', 'fyq测试2']
    wechat_name_list = ['fyq测试1']
    user = ('kf5', 'Qwer1234')
    yield wechat_name_list, user
