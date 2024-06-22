from modules import *


class GroupMuBanPage(PageObject):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_muban = self.page.get_by_text("新建模板")
        self.muban_name = self.page.locator('//div[@class="bscrmCSS-drawer-body"]//label[@title="模板名称"]/../following-sibling::div//input')
        self.muban_disc = self.page.locator('//div[@class="bscrmCSS-drawer-body"]//label[@title="模板描述"]/../following-sibling::div//input')
        self.msg_type = lambda msg_type: self.page.locator(f'//button[@title="{msg_type}"]')

        self.text_input = self.page.locator('//div[@class="bscrmCSS-modal-body"]//div[@class="DraftEditor-editorContainer"]/div')
        self.sure_in_text_input = self.page.locator('//div[@class="bscrmCSS-modal-footer"]//button/span[text()="确 定"]')
        self.sure_to_submit = self.page.locator('//div[@class="footer"]/button[@type="submit"]')

    def navigate(self):
        self.jump("/mantis/bscrm/groupSend/template")

    def create_muban_func(self, muban_name, muban_disc, text):
        self.create_muban.click()
        self.muban_name.type(muban_name)
        self.muban_disc.type(muban_disc)
        self.msg_type('文本编辑').click()
        self.text_input.type(text)
        self.sure_in_text_input.click()
        self.sure_to_submit.click()

