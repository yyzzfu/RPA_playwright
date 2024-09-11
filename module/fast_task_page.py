from module import *
from utils.tools import get_time


class FastTaskPage(BasePage):
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
        with allure.step('进入快捷任务界面'):
            self.jump("/mantis/bscrm/groupSend/quick/task")

    @property
    def get_table(self):
        return self.table(only_text='任务状态')

    def create_task_func(self, task_name, wechat_name, muban, **kwargs):
        regular = kwargs.get('regular')
        if isinstance(regular, bool) and regular:
            regular = 5
        elif isinstance(regular, int):
            regular = regular
        with allure.step('点击新建任务'):
            self.create_task.click()
        with allure.step(f'输入任务名称：{task_name}'):
            self.task_name.fill(task_name)
        with allure.step('点击选择企微账号'):
            self.choose_wechat.click()
        if isinstance(wechat_name, list):
            for name in wechat_name:
                with allure.step(f'在选择企微账号界面，选择企微账号：{name}'):
                    self.wechat(name).click()
        else:
            with allure.step(f'在选择企微账号界面，选择企微账号：{wechat_name}'):
                self.wechat(wechat_name).click()
        with allure.step('在选择企微账号界面，点击确定按钮'):
            self.sure_in.click()
        with allure.step('点击选择模板'):
            self.send_muban.click()
        with allure.step(f'在选择模板界面--模板搜索框中，输入模板名称：{muban}，并按回车键'):
            self.search.fill(muban)
            self.page.keyboard.press('Enter')
        with allure.step(f'在选择模板界面，勾选模板：{muban}'):
            self.muban(muban).click()
        with allure.step('在选择模板界面，点击确定按钮'):
            self.sure_in.click()
        if regular:
            with allure.step(f'在发送类型中，点击定时发送'):
                self.regular_button.click()
            self.time_input_button.click()
            send_time = get_time(regular)
            with allure.step(f'在日期选择界面--发送时间输入框中，输入发送时间：{send_time}'):
                self.time_input.fill(send_time)
            with allure.step(f'在日期选择界面，点击确定按钮'):
                self.sure_in_time.click()
        with allure.step(f'点击确定按钮--提交表单'):
            self.sure.click()
        with allure.step('等待确定按钮消失'):
            expect(self.sure).not_to_be_visible()
        with allure.step(f'在快捷任务列表--任务名称查询框中，输入任务名称：{task_name}，并按回车触发查询'):
            self.task_name_search.fill(task_name)
            self.search_button.click()
        with allure.step(f'在快捷任务列表中，任务名称：【{task_name}】查询成功'):
            expect(self.page.get_by_text(task_name)).to_be_visible()

