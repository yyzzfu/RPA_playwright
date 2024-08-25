from module import *


class GroupMuBanPage(BasePage):
    """群发模板"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.create_muban = self.page.get_by_text("新建模板")
        self.muban_name = self.page.locator(
            '//div[@class="bscrmCSS-drawer-body"]//label[@title="模板名称"]/../following-sibling::div//input')
        self.muban_disc = self.page.locator(
            '//div[@class="bscrmCSS-drawer-body"]//label[@title="模板描述"]/../following-sibling::div//input')
        self.msg_type = lambda msg_type: self.page.locator(f'//button[@title="{msg_type}"]')
        self.text_input = self.page.locator(
            '//div[@class="bscrmCSS-modal-body"]//div[@class="DraftEditor-editorContainer"]/div')
        self.sure_in_text_input = self.page.locator('//div[@class="bscrmCSS-modal-footer"]//button/span[text()="确 定"]')
        self.sure_to_submit = self.page.locator('//div[@class="footer"]/button[@type="submit"]')
        self.muban_search = self.page.get_by_placeholder('请输入模板名称')
        self.search_button = self.page.locator('//button/span[text()="查 询"]/..')
        self.result = lambda muban_name: self.page.locator(f'//div[@class="bscrmCSS-table-content"]//td[text()="{muban_name}"]')

    def navigate(self):
        with allure.step('进入群发模板界面'):
            self.jump("/mantis/bscrm/groupSend/template")

    def create_muban_func(self, muban_name, muban_disc, text):
        with allure.step('点击新建模板'):
            self.create_muban.click()
        with allure.step(f'输入模板名称：{muban_name}'):
            self.muban_name.type(muban_name)
        with allure.step(f'输入模板描述：{muban_disc}'):
            self.muban_disc.type(muban_disc)
        with allure.step(f'在内容中，点击文本按钮'):
            self.msg_type('文本编辑').click()
        with allure.step(f'在文本编辑界面--文本输入框中，输入内容：{text}'):
            self.text_input.type(text)
        with allure.step(f'在文本编辑界面，点击确定按钮'):
            self.sure_in_text_input.click()
        with allure.step(f'点击确定按钮--提交表单'):
            self.sure_to_submit.click()
        expect(self.sure_to_submit).not_to_be_visible()
        with allure.step(f'在群发模板列表--模板名称查询框中，输入模板名称：{muban_name}，并点击查询按钮'):
            self.muban_search.fill(muban_name)
            self.search_button.click()
        with allure.step(f'在群发模板列表，模板名称：【{muban_name}】查询成功'):
            expect(self.result(muban_name)).to_be_visible()
