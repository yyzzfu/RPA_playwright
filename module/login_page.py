from module import *


class LoginPage(BasePage):
    """登录页面"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.username = self.page.get_by_placeholder("请输入用户名")
        self.password = self.page.get_by_placeholder("请输入密码")
        self.login_button = self.page.get_by_role("button", name="登 录")
        self.login_by_username = self.page.locator(
            '//div[@class="ant-spin-container"]//div[@role="tab" and text()="账号密码登录"]')

    def navigate(self):
        self.jump("/")

    def login(self, username: str, password: str, login_type: int = 2):
        """
        通过页面进行登录
        :param username:
        :param password:
        :return:
        """
        with allure.step('进入登录界面'):
            self.navigate()

        num = 0
        while True:
            try:
                if login_type > 1:  # 登录方式大于1
                    expect(self.login_by_username).to_be_visible(timeout=10_000)
                    self.login_by_username.click()
            except:
                pass
            try:
                with allure.step(f'输入用户名：{username}'):
                    self.username.fill(username)
                with allure.step(f'输入密码：{password}'):
                    self.password.fill(password)
                with allure.step('点击登录按钮'):
                    self.login_button.click()
                expect(self.login_button).not_to_be_visible()
                expect(self.page.locator(
                    f'//div[@class="mantis-main-stage-header"]//span[contains(text(), "{username}")]')).to_be_visible(
                    timeout=10_000)
                break
            except:
                num += 1
                self.page.reload()
                if num == 10:
                    raise Exception('登录失败！！！')