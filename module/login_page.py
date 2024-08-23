from module import *


class LoginPage(PageObject):
    """登录页面"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.username = self.page.get_by_placeholder("请输入用户名")
        self.password = self.page.get_by_placeholder("请输入密码")
        self.login_button = self.page.get_by_role("button", name="登 录")
        self.login_by_username = self.page.locator('//div[@class="ant-spin-container"]//div[@role="tab" and text()="账号密码登录"]')

    def navigate(self):
        self.jump("/")

    def page_login(self, username: str, password: str):
        """
        通过页面进行登录
        :param username:
        :param password:
        :return:
        """
        self.navigate()
        num = 0
        while True:
            try:
                try:
                    expect(self.login_by_username).to_be_visible(timeout=10_000)
                    self.login_by_username.click()
                except:
                    pass
                self.username.fill(username)
                self.password.fill(password)
                self.login_button.click()
                expect(self.page.locator(
                    f'//div[@class="mantis-main-stage-header"]//span[contains(text(), "{username}")]')).to_be_visible(
                    timeout=10_000)
                break
            except:
                num += 1
                self.page.reload()
                if num == 10:
                    raise Exception('登录失败！！！')