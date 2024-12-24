from module import *


class HomePage(BasePage):
    """首页"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.login_info = self.page.locator('//span[@id="loginInfo"]')
        self.username_right = lambda username: self.page.locator(
            f'//div[@class="mantis-main-stage-header"]//span[contains(text(), "{username}")]')
        self.WeCom_workbench = self.page.locator('//div[@class="loginInfoBox"]/div').filter(has_text="企微工作台")

    def navigate(self):
        with allure.step('进入首面'):
            self.jump("/mantis")




