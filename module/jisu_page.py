from module import *
from utils.tools import get_time


class JiSuPage(BasePage):
    """极速群发"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.create_task = self.page.get_by_text("新建任务")
        self.group = self.page.locator('//li[@class="bscrmCSS-dropdown-menu-item"][text()="群聊群发"]')
        self.person = self.page.locator('//li[@class="bscrmCSS-dropdown-menu-item"][text()="私聊群发"]')
        self.task_name = self.page.get_by_placeholder("请输入任务名称")
        self.choose_wechat = self.page.locator("//button/span[text()='选择企微账号']")
        self.wechat = lambda wechat_name: self.page.locator(
            f'//table//td[text()="{wechat_name}"]/../td[@class="bscrmCSS-table-selection-column"]')
        self.send_object_group = self.page.locator("//button/span[text()='选择客户群']")
        self.send_object_person = self.page.locator("//button/span[text()='选择客户']")
        self.group_name = self.page.get_by_placeholder('可输入多个，按回车或后面的加号')
        self.sure = self.page.locator('//div[@class="bscrmCSS-modal-content"]//button/span[text()="确 定"]')
        self.check_all = self.page.get_by_text('全选所有')
        self.sure_in_choose_send_object = self.page.locator('//div[@class="footer"]//button/span[text()="确 定"]')
        self.send_content_text = self.page.locator('//div[@class="sendContent"]//span[text()="文本"]')
        self.text_input = self.page.locator('//div[@class="sendContent"]//div[@id="editDiv"]')
        self.sure_in_text_input = self.page.locator('//div[@class="bscrmCSS-modal-content"]//button/span[text()="确 定"]')
        self.send_content_picture = self.page.locator('//div[@class="sendContent"]//span[text()="图片"]')
        self.add_button = self.page.locator('//div[@class="bscrmCSS-modal-content"]//div[@class="sop-upload-btn"]')
        self.upload_suc = self.page.locator('//div[@class="bscrmCSS-message"]//span[text()="上传成功~"]')
        self.send_content_video = self.page.locator('//div[@class="sendContent"]//span[text()="视频"]')
        self.send_content_link = self.page.locator('//div[@class="sendContent"]//span[text()="链接"]')
        self.link_title = self.page.get_by_placeholder('请输入链接标题')
        self.link_address = self.page.get_by_placeholder('请输入链接', exact=True)
        self.link_content = self.page.get_by_placeholder('请输入内容简介')
        self.send_content_file = self.page.locator('//div[@class="sendContent"]//span[text()="文件"]')
        self.file_name = self.page.get_by_placeholder('请输入文件名称')
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

    def upload(self, path):
        num = 0
        with allure.step('上传图片/视频/文件'):
            while True:
                try:
                    self.page.wait_for_timeout(1_000)
                    with self.page.expect_file_chooser() as f:
                        self.add_button.click()
                        break
                except Exception as e:
                    num += 1
                    if num == 3:
                        raise e
            f.value.set_files(path)
            expect(self.upload_suc).to_be_visible()
            expect(self.add_button).not_to_be_visible()
        with allure.step('在上传界面，点击确定按钮'):
            self.sure_in_text_input.click()

    def create_task_func(self, task_name, wechat_name, task_type, send_name_list='', text='', picture='',
                         video='', link: dict='', file: dict='', **kwargs):
        regular = kwargs.get('regular')
        if isinstance(regular, bool) and regular:
            regular = 5
        elif isinstance(regular, int):
            regular = regular
        num = 0
        timeout = 5_000
        while True:
            try:
                self.create_task.hover(timeout=timeout)
                send_object = None
                if task_type == '群聊群发':
                    send_object = self.send_object_group
                    self.group.click(timeout=timeout)
                elif task_type == '私聊群发':
                    send_object = self.send_object_person
                    self.person.click(timeout=timeout)
                break
            except Exception as e:
                num += 1
                if num == 30:
                    raise e
        self.task_name.fill(task_name)
        self.choose_wechat.click()
        if isinstance(wechat_name, list):
            for name in wechat_name:
                self.wechat(name).click()
        else:
            self.wechat(wechat_name).click()
        self.sure.click()
        send_object.click()
        for name in send_name_list:
            self.group_name.fill(name)
            self.page.keyboard.press('Enter')
        self.check_all.click()
        self.sure_in_choose_send_object.click()

        if text:
            with allure.step(f'在群发内容中，输入内容：{text}'):
                self.text_input.type(text)
        if picture:
            with allure.step('在追加内容中，点击图片按钮'):
                self.send_content_picture.click()
                self.upload(picture)
        if video:
            with allure.step('在追加内容中，点击视频按钮'):
                self.send_content_video.click()
                self.upload(video)
        if file:
            file_name = file.get('file_name')
            file_path = file.get('file_path')
            with allure.step('在追加内容中，点击文件按钮'):
                self.send_content_file.click()
            with allure.step(f'在上传文件界面--文件名称输入框中，输入文件名称：{file_name}'):
                self.file_name.fill(file_name)
            self.upload(file_path)
        if link:
            with allure.step('在追加内容中，点击链接按钮'):
                self.send_content_link.click()
            self.link_title.fill(link['title'])
            self.link_address.fill(link['address'])
            self.link_content.fill(link['content'])
            self.upload(link['picture_path'])
        if regular:
            self.regular_button.click()
            self.time_input_button.click()
            self.time_input.fill(get_time(regular))
            self.sure_in_time.click()
        self.sure_to_submit.click()
        expect(self.sure_to_submit).not_to_be_visible()
        self.search_task_name.fill(task_name)
        self.page.keyboard.press('Enter')
        expect(self.task_name_in_card(task_name)).to_be_visible()

