from playwright.sync_api import expect, Page


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
        self.page.goto(path, wait_until='load')

    def page_login(self, username: str, password: str, url):
        """
        通过页面进行登录
        :param username:
        :param password:
        :return:
        """
        num = 0
        while True:
            try:
                self.page.goto(url)
                self.page.reload()
                self.page.get_by_placeholder("请输入用户名").fill(username)
                self.page.get_by_placeholder("请输入密码").fill(password)
                self.page.get_by_role("button", name="登 录").click()
                expect(self.page.locator(
                    f'//div[@class="mantis-main-stage-header"]//span[contains(text(), "{username}")]')).to_be_visible(
                    timeout=10000)
                break
            except:
                num += 1
                self.page.reload()
                if num == 10:
                    raise Exception('登录失败！！！')
                continue
