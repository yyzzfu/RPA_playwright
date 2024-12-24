import os
import sys
import re
import random
from playwright.sync_api import Page, expect, BrowserContext, Locator
import allure
import pytest
from data_module.user_data import UserData
from module.WeCom_workbench_page import WeComWorkbenchPage
from module.base_page import BasePage
from module.home_page import HomePage
from module.train_camp_page import TrainCampPage
from utils.tools import get_path, 返回当前日期和减N天的日期
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
        self.train_camp_page = TrainCampPage(self.page)
        self.home_page = HomePage(self.page)
        self.WeCom_workbench_page = WeComWorkbenchPage(self.page)

    @staticmethod
    def new_context_and_return_page_ins(new_context, user):
        username, password = user.get('user')
        login_type_num = user.get('login_type_num')
        login_url = user.get('login_url')
        with allure.step(f'访问地址：{login_url}'):
            allure.attach(f'账号：{username}，密码：{password}', name='账号密码', attachment_type=allure.attachment_type.TEXT)
        with FileLock(get_path(f".temp/{username}.lock")):
            if os.path.exists(get_path(f".temp/{username}.json")):
                context: BrowserContext = new_context(storage_state=get_path(f".temp/{username}.json"))
                page = context.new_page()
                my_page = PageIns(page)
                my_page.home_page.navigate()
                login_by_username = page.locator(
                    '//div[@class="ant-spin-container"]//div[@role="tab" and text()="账号密码登录"]')
                try:
                    expect(my_page.login_page.username.or_(my_page.home_page.username_right(username))).to_be_visible(timeout=10_000)
                    if my_page.home_page.username_right(username).is_visible():
                        with allure.step('已使用本地的storage_state，无需登录！'):
                            ...
                    elif my_page.login_page.username.count() or login_by_username.count():
                        my_page.login_page.login(username, password, login_type_num)
                        my_page.page.context.storage_state(path=get_path(f".temp/{username}.json"))
                except AssertionError:
                    my_page.login_page.login(username, password, login_type_num)
                    my_page.page.context.storage_state(path=get_path(f".temp/{username}.json"))
            else:
                context: BrowserContext = new_context()
                page = context.new_page()
                my_page = PageIns(page)
                my_page.login_page.login(username, password, login_type_num)
                my_page.page.context.storage_state(path=get_path(f".temp/{username}.json"))
            return my_page

    @staticmethod
    def login_and_return_page_ins(page: Page, user):
        username, password = user.get('user')
        login_type_num = user.get('login_type_num')
        login_url = user.get('login_url')
        my_page = PageIns(page)
        with allure.step(f'访问地址：{login_url}'):
            allure.attach(f'账号：{username}，密码：{password}', name='账号密码', attachment_type=allure.attachment_type.TEXT)
        my_page.login_page.login(username, password, login_type_num=login_type_num)
        return my_page
