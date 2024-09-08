import pytest
import time
import os
import sys
import re
import random
from playwright.sync_api import Page, expect, BrowserContext, Locator
import allure

from data_module.my_data import MyData
from module.base_page import BasePage
from utils.tools import get_path
from filelock import FileLock
from utils.global_map import GlobalMap
from module.fast_task_page import FastTaskPage
from module.gaoji_page import GaoJiPage
from module.group_muban_page import GroupMuBanPage
from module.group_rename_task_page import GroupNameTaskPage
from module.jisu_page import JiSuPage
from module.pull_group_page import PullGroupPage
from module.login_page import LoginPage


class PageIns:
    def __init__(self, page: Page):
        self.page = page
        self.fast_task_page = FastTaskPage(self.page)
        self.gaoji_page = GaoJiPage(self.page)
        self.group_muban_page = GroupMuBanPage(self.page)
        self.group_rename_task_page = GroupNameTaskPage(self.page)
        self.jisu_page = JiSuPage(self.page)
        self.pull_group_page = PullGroupPage(self.page)
        self.login_page = LoginPage(self.page)

    @staticmethod
    def new_context_and_return_page_ins(new_context):
        global_map = GlobalMap()
        # 被测环境 = global_map.get("env")
        # 用户名 = MyData().userinfo(被测环境, 用户别名)["username"]
        # 密码 = MyData().userinfo(被测环境, 用户别名)["password"]
        # with FileLock(get_path(f".temp/{被测环境}-{用户别名}.lock")):
        #     if os.path.exists(get_path(f".temp/{被测环境}-{用户别名}.json")):
        #         context: BrowserContext = new_context(storage_state=get_path(f".temp/{被测环境}-{用户别名}.json"))
        #         page = context.new_page()
        #         my_page = PageIns(page)
        #         my_page.我的任务.navigate()
        #         expect(my_page.登录页.用户名输入框.or_(my_page.登录页.通知铃铛)).to_be_visible()
        #         if my_page.登录页.用户名输入框.count():
        #             my_page.登录页.登录(用户名, 密码)
        #             my_page.page.context.storage_state(path=get_path(f".temp/{被测环境}-{用户别名}.json"))
        #     else:
        #         context: BrowserContext = new_context()
        #         page = context.new_page()
        #         my_page = PageIns(page)
        #         my_page.登录页.登录(用户名, 密码)
        #         my_page.page.context.storage_state(path=get_path(f".temp/{被测环境}-{用户别名}.json"))
        # return my_page
        username = MyData().userinfo().get('username')
        password = MyData().userinfo().get('password')
        with FileLock(get_path(f".temp/{username}.lock")):
            if os.path.exists(get_path(f".temp/{username}.json")):
                context: BrowserContext = new_context(storage_state=get_path(f".temp/{username}.json"))
                page = context.new_page()
                my_page = PageIns(page)
                my_page.fast_task_page.jump('/mantis')
                try:
                    expect(my_page.page.locator(
                        f'//div[@class="mantis-main-stage-header"]//span[contains(text(), "{username}")]')).to_be_visible(
                        timeout=20_000)
                except:
                    my_page.login_page.login(username, password)
                    my_page.page.context.storage_state(path=get_path(f".temp/{username}.json"))
            else:
                context: BrowserContext = new_context()
                page = context.new_page()
                my_page = PageIns(page)
                my_page.login_page.login(username, password)
                my_page.page.context.storage_state(path=get_path(f".temp/{username}.json"))
        return my_page

    @staticmethod
    def login_and_return_page_ins(page: Page, kf='', kf_for_data='', login_type=1):
        test_data = MyData().data_for_test(kf_for_data)
        password = test_data.get('password')
        my_page = PageIns(page)
        my_page.login_page.login(kf, password, login_type)
        my_page.test_data = test_data
        # with FileLock(get_path(f".temp/{username}.lock")):
        #     my_page = PageIns(page)
        #     my_page.login_page.login(username, password)
        #     my_page.test_data = test_data
        # my_page.page.context.storage_state(path=get_path(f".temp/{username}.json"))
        return my_page
