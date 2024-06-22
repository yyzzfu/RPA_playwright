from modules import *


class GaoJiPage(PageObject):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_task = self.page.get_by_text("新建任务")
        self.group = self.page.locator('//li[@class="bscrmCSS-dropdown-menu-item"][text()="群聊群发"]')
        self.person = self.page.locator('//li[@class="bscrmCSS-dropdown-menu-item"][text()="私聊群发"]')
        self.notice = self.page.locator('//li[@class="bscrmCSS-dropdown-menu-item"][text()="群发公告"]')
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
        self.text_input = self.page.locator('//div[@id="editDiv"]')
        self.notice_input = self.page.locator('//div[@class="sendContent"]//div[@id="editDiv"]')
        self.notice_text = self.page.locator('//div[@class="bscrmCSS-modal-content"]//div[@id="editDiv"]')
        self.sure_in_text_input = self.page.locator('//div[@class="bscrmCSS-modal-content"]//button/span[text()="确 定"]')

        self.send_content_picture = self.page.locator('//div[@class="sendContent"]//span[text()="图片"]')
        # self.add_button = self.page.locator('//div[@class="bscrmCSS-modal-content"]//i[@class="anticon anticon-plus"]')
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
        self.load_tip = self.page.locator('//div[@class="ant-spin ant-spin-spinning"]/span[@class="ant-spin-dot ant-spin-dot-spin"]')

    def navigate(self):
        self.jump("/mantis/bscrm/highMassTexting")

    def create_task_func(self, task_name, wechat_name_list, name_list, send_content_dic, task_type):
        self.create_task.hover()
        if task_type == '群聊群发':
            send_object = self.send_object_group
            self.group.click()
        elif task_type == '私聊群发':
            send_object = self.send_object_person
            self.person.click()
        else:
            send_object = self.send_object_group
            self.notice.click()
        self.task_name.fill(task_name)
        self.choose_wechat.click()
        for wechat_name in wechat_name_list:
            self.wechat(wechat_name).click()
        self.sure.click()
        send_object.click()
        for name in name_list:
            self.group_name.fill(name)
            self.page.keyboard.press('Enter')
        self.check_all.click()
        self.sure_in_choose_send_object.click()
        notice_input_count = 0
        for content in send_content_dic:
            text_input = self.text_input
            if task_type == '群发公告':
                if notice_input_count == 0:
                    self.notice_input.type(send_content_dic['notice'])
                text_input = self.notice_text
                notice_input_count += 1
            if content == 'text':
                self.send_content_text.click()
                text_input.type(send_content_dic[content])
                self.sure_in_text_input.click()
            elif content in ['picture', 'video', 'file']:
                if content == 'picture':
                    path = send_content_dic[content]
                    self.send_content_picture.click()
                elif content == 'video':
                    path = send_content_dic[content]
                    self.send_content_video.click()
                else:
                    path = send_content_dic[content]['file_path']
                    file_name = send_content_dic[content]['file_name']
                    self.send_content_file.click()
                    self.file_name.fill(file_name)
                with self.page.expect_file_chooser() as f:
                    self.add_button.click()
                f.value.set_files(path)
                expect(self.upload_suc).to_be_visible()
                expect(self.upload_suc).not_to_be_visible()
                self.sure_in_text_input.click()
            elif content == 'link':
                self.send_content_link.click()
                self.link_title.fill(send_content_dic[content]['title'])
                self.link_address.fill(send_content_dic[content]['address'])
                self.link_content.fill(send_content_dic[content]['content'])
                with self.page.expect_file_chooser() as f:
                    self.add_button.click()
                f.value.set_files(send_content_dic[content]['picture_path'])
                expect(self.upload_suc).to_be_visible()
                expect(self.upload_suc).not_to_be_visible()
                self.sure_in_text_input.click()
        self.sure_to_submit.click()
        expect(self.sure_to_submit).not_to_be_visible()
        self.search_task_name.fill(task_name)
        self.page.keyboard.press('Enter')
        expect(self.task_name_in_card(task_name)).to_be_visible()

    def create_group_task(self, task_name, wechat_name_list, group_name_list, send_content_dic):
        self.create_task_func(task_name, wechat_name_list, group_name_list, send_content_dic, task_type='群聊群发')

    def create_person_task(self, task_name, wechat_name_list, person_name_list, send_content_dic):
        self.create_task_func(task_name, wechat_name_list, person_name_list, send_content_dic, task_type='私聊群发')

    def create_notice_task(self, task_name, wechat_name_list, person_name_list, send_content_dic):
        self.create_task_func(task_name, wechat_name_list, person_name_list, send_content_dic, task_type='群发公告')


    # with page.expect_download() as f:
    #     page.locator("a").get_by_text("下载模板").click()
    # file_path = get_path(f"download/{time.time_ns()}.xlsx")
    # f.value.save_as(file_path)
    # page.set_input_files('//input[@type="file"]', get_path("upload/testupload.xlsx"))
    # expect(page.get_by_text("testupload.xlsx")).to_be_visible()
