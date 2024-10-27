from module import *


class GaoJiPage(BasePage):
    """高级群发"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.create_task = self.page.get_by_text("新建任务")
        self.send = lambda task_type: self.page.locator(
            f'//li[@class="bscrmCSS-dropdown-menu-item"][text()="{task_type}"]')
        self.task_name = self.page.get_by_placeholder("请输入任务名称")
        self.send_content = lambda content_type: self.page.locator(f'//div[@class="sendContent"]//span[text()="{content_type}"]')
        self.text_input = self.page.locator('//div[@id="editDiv"]').last
        self.notice_input = self.page.locator('//div[@class="sendContent"]//div[@id="editDiv"]')
        self.notice_text = self.page.locator('//div[@class="bscrmCSS-modal-content"]//div[@id="editDiv"]')
        self.sure_in_text_input = self.page.locator('//div[@class="bscrmCSS-modal-content"]//button/span[text()="确 定"]')
        self.sure_to_submit = self.page.locator('//div[@class="btnBox"]//button/span[text()="确 定"]')
        self.search_task_name = self.page.get_by_placeholder('请输入任务名称')
        self.task_name_in_card = lambda task_name: self.page.locator(
            f'//div[@class="HighMassTexting_main_L"]//span[text()="{task_name}"]')
        self.load_tip = self.page.locator(
            '//div[@class="ant-spin ant-spin-spinning"]/span[@class="ant-spin-dot ant-spin-dot-spin"]')
        self.single_send = self.page.locator('//input[@id="singleSendFlag"]/..')

    def navigate(self):
        with allure.step('进入高级群发界面'):
            self.jump("/mantis/bscrm/highMassTexting")

    def send_content_text(self, text, task_type):
        placeholder = lambda placeholder1: self.page.locator(f'//div[@class="main_tool_L"]/span[text()="{placeholder1}"]')  # 占位符按钮

        self.send_content('文本').click()
        self.text_input.fill(text)
        self.add_emoji(1)
        if task_type in ['群聊群发', '群发公告']:
            placeholder('插入员工姓名')
        placeholder('@所有人')
        self.add_live_link()
        self.add_yingqi_link()
        self.add_random_emoji()
        self.sure_in_text_input.click()

    def create_task_func(self, task_type, task_name, wechat_name, send_object_type, send_name_list='', text='',
                         picture='', video='', link: dict = '', file: dict = '', notice='', one_by_one='', regular='',
                         **kwargs):
        with allure.step(f'鼠标hover到新建任务按钮上，并点{task_type}'):
            with self.page.expect_response(r'https://qaks.bjmantis.net/e-wechat/device/queryParams') as response_info:
                self.hover_with_retry(self.create_task, self.send(task_type))
                response = response_info.value
                RPA_TASK_BUG_SEND_FLAG = response.json().get('data').get('RPA_TASK_BUG_SEND_FLAG')  # 卡bug参数
        if RPA_TASK_BUG_SEND_FLAG == 'Y':
            video = None
            file = None
        with allure.step(f'输入任务名称：{task_name}'):
            self.task_name.fill(task_name)

        self.choose_wecome(wechat_name)
        self.choose_send_object(send_object_type, send_name_list)
        if notice:
            with allure.step(f'输入群公告内容：{notice}'):
                self.notice_input.type(notice)
            self.add_live_link()
            self.add_yingqi_link()
        if text:
            self.send_content_text(text, task_type)
        if picture:
            self.add_picture(picture)
        if video:
            self.add_video(video)
        if file:
            self.add_file(file)
        if link:
            self.add_link(link)
        if one_by_one:
            with allure.step('在模式设置--发送模板中，勾选【指定的群单独发送】'):
                self.single_send.click()
        if regular:
            self.regular_send(regular)
        with allure.step(f'点击确定按钮--提交表单'):
            self.sure_to_submit.click()
        expect(self.sure_to_submit).not_to_be_visible()
        with allure.step(f'在高级群发列表--任务名称查询框中，输入任务名称：{task_name}，并按回车触发查询'):
            self.search_task_name.fill(task_name)
            self.page.keyboard.press('Enter')
        with allure.step(f'在高级群发列表中，任务名称：【{task_name}】查询成功'):
            expect(self.task_name_in_card(task_name)).to_be_visible()

