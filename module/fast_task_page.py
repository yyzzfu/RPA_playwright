from module import *
from utils.tools import get_time


class FastTaskPage(PageObject):
    """快捷任务"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.create_task = self.page.get_by_text("新建任务")
        self.task_name_search = self.page.get_by_placeholder("请输入任务名称")
        self.task_name = self.page.get_by_placeholder("请输入任务名称").last
        self.choose_wechat = self.page.locator("//button/span[text()='选择企微账号']")
        self.wechat = lambda wechat_name: self.page.locator(
            f'//table//td[text()="{wechat_name}"]/../td[@class="bscrmCSS-table-selection-column"]')
        self.send_muban = self.page.locator('//div[@class="bscrmCSS-modal-body"]//button/span[text()="选择模板"]/..')
        self.search = self.page.get_by_placeholder('请输入查询内容')
        self.muban = lambda muban: self.page.locator(
            f'//table//td[text()="{muban}"]/../td[@class="bscrmCSS-table-selection-column"]')
        self.sure_in = self.page.locator(
            '//div[@class="bscrmCSS-modal-content"]//button[@type="button"]/span[text()="确 定"]/..').last
        self.sure = self.page.locator(
            '//div[@class="bscrmCSS-modal-content"]//button[@type="button"]/span[text()="确 定"]/..')
        self.search_button = self.page.locator('//button/span[text()="查 询"]/..')
        self.regular_button = self.page.locator(
            '//span[text()="定时发送"]/../span[@class="bscrmCSS-radio"]')
        self.time_input_button = self.page.get_by_placeholder('请选择发送时间')
        self.time_input = self.page.locator('//input[@class="bscrmCSS-calendar-input "]')
        self.sure_in_time = self.page.locator(
            '//span[@class="bscrmCSS-calendar-footer-btn"]/a[@class="bscrmCSS-calendar-ok-btn"]')

    def navigate(self):
        self.jump("/mantis/bscrm/groupSend/quick/task")

    def create_task_func(self, task_name, wechat_name_list, muban, **kwargs):
        regular = kwargs.get('regular')
        if isinstance(regular, bool) and regular:
            regular = 5
        elif isinstance(regular, int):
            regular = regular
        self.create_task.click()
        self.task_name.fill(task_name)
        self.choose_wechat.click()
        for wechat_name in wechat_name_list:
            self.wechat(wechat_name).click()
        self.sure_in.click()
        self.send_muban.click()
        self.search.fill(muban)
        self.muban(muban).click()
        self.sure_in.click()
        if regular:
            self.regular_button.click()
            self.time_input_button.click()
            self.time_input.fill(get_time(regular))
            self.sure_in_time.click()
        self.sure.click()
        expect(self.sure).not_to_be_visible()
        self.task_name_search.fill(task_name)
        self.search_button.click()
        expect(self.page.get_by_text(task_name)).to_be_visible()
