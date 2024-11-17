from module import *


class JiSuPage(BasePage):
    """极速群发"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.create_task = self.page.get_by_text("新建任务")
        self.send = lambda task_type: self.page.locator(
            f'//li[@class="bscrmCSS-dropdown-menu-item"][text()="{task_type}"]')
        self.task_name = self.page.get_by_placeholder("请输入任务名称")
        self.text_input = self.page.locator('//div[@class="sendContent"]//div[@id="editDiv"]')
        self.sure_to_submit = self.page.locator('//div[@class="btnBox"]//button/span[text()="确 定"]')
        self.search_task_name = self.page.get_by_placeholder('请输入任务名称')
        self.task_name_in_card = lambda task_name: self.page.locator(
            f'//div[@class="HighMassTexting_main_L"]//span[text()="{task_name}"]')
        self.load_tip = self.page.locator(
            '//div[@id="prmt-container"]//div[@class="ant-spin ant-spin-spinning"]/span[@class="ant-spin-dot ant-spin-dot-spin"]')
        self.regular_button = self.page.locator(
            '//div[@class="timeSeting"]//span[text()="定时发送"]/../span[@class="bscrmCSS-radio"]')
        self.time_input_button = self.page.get_by_placeholder('请选择发送时间')
        self.time_input = self.page.locator('//input[@class="bscrmCSS-calendar-input "]')
        self.sure_in_time = self.page.locator(
            '//span[@class="bscrmCSS-calendar-footer-btn"]/a[@class="bscrmCSS-calendar-ok-btn"]')

    def navigate(self):
        with allure.step('进入极速群发界面'):
            self.jump("/mantis/bscrm/topspeedMassTexting")

    def create_task_func(self, task_name, wechat_name, send_object_type, task_type, send_name_list='', text='',
                         picture='', video='', link: dict = '', file: dict = '', mini_program='', regular='',
                         **kwargs):

        with allure.step(f'鼠标hover到新建任务按钮上，并点击{task_type}'):
            self.hover_with_retry(self.create_task, self.send(task_type))
        with allure.step(f'输入任务名称：{task_name}'):
            self.task_name.fill(task_name)
        self.choose_wecome(wechat_name)
        self.choose_send_object(send_object_type, send_name_list)
        if text:
            with allure.step(f'点击文本按钮'):
                with allure.step(f'输入群发内容：{text}'):
                    self.text_input.type(text)
                self.add_emoji(1)
                self.add_live_link()
                self.add_yingqi_link()
        if picture:
            self.add_picture(picture)
        if video:
            self.add_video(video)
        if file:
            self.add_file(file)
        if link:
            self.add_link(link)
        if mini_program:
            self.add_mini_program()
        if regular:
            self.regular_send(regular)
        with allure.step(f'点击确定按钮--提交表单'):
            self.sure_to_submit.click()
        expect(self.sure_to_submit).not_to_be_visible()
        with allure.step(f'在列表--任务名称查询框中，输入任务名称：{task_name}，并按回车触发查询'):
            self.search_task_name.fill(task_name)
            self.page.keyboard.press('Enter')
        with allure.step(f'在列表中，任务名称：【{task_name}】查询成功'):
            expect(self.task_name_in_card(task_name)).to_be_visible()
