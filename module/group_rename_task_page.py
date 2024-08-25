from module import *
from utils.tools import get_time


class GroupNameTaskPage(BasePage):
    """群名任务"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.create_task = self.page.get_by_text("新建任务")
        self.task_name_search = self.page.get_by_placeholder("请输入任务名称")
        self.task_name = self.page.get_by_placeholder("请输入任务名称").last
        self.choose_wechat = self.page.locator("//button/span[text()='选择螳螂智能助理']")
        self.wechat = lambda wechat_name: self.page.locator(
            f'//table//td[contains(text(),"{wechat_name}")]/../td[@class="bscrmCSS-table-selection-column"]')
        self.search = self.page.get_by_placeholder('请输入查询内容')
        self.search_tips = self.page.locator(
            '//div[@class="bscrmCSS-spin-container bscrmCSS-spin-blur"]//div[@class="bscrmCSS-spin-nested-loading"]')
        self.result = lambda task_name: self.page.locator(f'//div[@class="MT_containers"]//td[text()="{task_name}"]')
        self.group = lambda group: self.page.locator(
            f'//tbody[@class="bscrmCSS-table-tbody"]//td[contains(text(), "{group}")]/../td[@class="bscrmCSS-table-selection-column"]').all()
        self.choose_group = self.page.locator('//div[@class="bscrmCSS-form-item-control"]//button')
        self.new_group_name = self.page.get_by_placeholder('请输入新群名')
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
        with allure.step('进入群名任务界面'):
            self.jump("/mantis/bscrm/groupSend/group/name/task")

    def create_task_func(self, task_name, wechat_name_list, group_name, new_group_name, **kwargs):
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
        self.choose_group.click()
        num = 0
        while True:
            try:
                self.search.fill(group_name)
                self.page.wait_for_timeout(1_000)
                self.page.keyboard.press('Enter')
                expect(self.search_tips).to_be_visible()
                expect(self.search_tips).not_to_be_visible()
                if self.group(group_name):
                    break
            except Exception as e:
                self.search.clear()
                num += 1
                if num == 5:
                    raise e

        for i in self.group(group_name):
            i.click()
        self.sure_in.click()
        self.new_group_name.fill(new_group_name)
        if regular:
            self.regular_button.click()
            self.time_input_button.click()
            self.time_input.fill(get_time(regular))
            self.sure_in_time.click()
        self.sure.click()
        expect(self.sure).not_to_be_visible()
        self.task_name_search.fill(task_name)
        self.search_button.click()
        expect(self.result(task_name)).to_be_visible()
