from playwright.sync_api import expect, Page
import os
import time
from utils.tools import get_path


class PageObject:
    def __init__(self, page: Page):
        self.page = page
        def_timeout = 30000
        self.page.set_default_timeout(def_timeout)
        self.page.set_default_navigation_timeout(def_timeout)
        expect.set_options(30000)

    def navigate(self):
        self.jump()

    def jump(self, path: str = None):
        if path[0] != "/":
            path = f"/{path}"
        # self.page.goto(f'{self.page.url.split(".com")[0]}.com{path}')
        self.page.goto(path, wait_until='commit')

    def page_login(self, username: str, password: str, url):
        """
        通过页面进行登录
        :param username:
        :param password:
        :return:
        """
        while True:
            try:
                self.page.goto(url)
                self.page.get_by_placeholder("请输入用户名").type(username, delay=30)
                self.page.get_by_placeholder("请输入密码").fill(password)
                self.page.get_by_role("button", name="登 录").click()
                expect(self.page.locator(
                    f'//div[@class="mantis-main-stage-header"]//span[contains(text(), "{username}")]')).to_be_visible(
                    timeout=10000)
                break
            except:
                self.page.reload()
                continue
