from module import *
from utils.tools import get_time


class GaoJiPage(BasePage):
    """高级群发"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.create_task = self.page.get_by_text("新建任务")
        self.send = lambda task_type: self.page.locator(
            f'//li[@class="bscrmCSS-dropdown-menu-item"][text()="{task_type}"]')
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
        self.send_content = lambda content_type: self.page.locator(f'//div[@class="sendContent"]//span[text()="{content_type}"]')
        self.text_input = self.page.locator('//div[@id="editDiv"]').last
        self.emoji_button = self.page.locator('//img[@class="emoji_btn"]')  # 表情按钮
        self.emoji = self.page.locator('//div[@class="emojiBox"]/div')
        self.placeholder = lambda placeholder: self.page.locator(f'//div[@class="main_tool_L"]/span[text()="{placeholder}"]')  # 占位符按钮
        self.start_date = self.page.locator('//input[@placeholder="开始日期"]')
        self.date = lambda date: self.page.locator(f'//div[@class="bscrmCSS-calendar-range-part bscrmCSS-calendar-range-left"]//td[@title="{date}"]')
        self.live_video = self.page.locator('//td[@class="bscrmCSS-table-selection-column"]').first   # 直播视频课
        self.sure_in_choose_live_video = self.page.locator('//div[@class="bscrmCSS-modal MT_Modal SelectLiveModal"]//div[@class="bscrmCSS-modal-footer"]//span[text()="确 定"]/..')
        self.xunlianying_select = self.page.locator('//div[text()="请选择训练营"]')
        self.xunlianying = self.page.locator('//ul[@class="bscrmCSS-select-dropdown-menu  bscrmCSS-select-dropdown-menu-root bscrmCSS-select-dropdown-menu-vertical"]/li').first
        self.yingqi_select = self.page.locator('//div[text()="请选择营期"]')
        self.yingqi = self.page.locator('//ul[@class="bscrmCSS-select-dropdown-menu  bscrmCSS-select-dropdown-menu-root bscrmCSS-select-dropdown-menu-vertical"]').last.locator('//li').first
        self.yingqi_video = self.page.locator('//div[@class="SelectLiveModal_main_R"]//span[@class="bscrmCSS-radio"]').first
        self.sure_in_choose_yingqi_video = self.page.locator('//div[@class="bscrmCSS-modal MT_Modal SelectLiveModal SelectCampModal"]//div[@class="bscrmCSS-modal-footer"]//span[text()="确 定"]/..')
        self.random_emoji = self.page.locator('//div[@class="main_tool_L"]//div[text()="随机表情"]')
        self.random_emoji_edit = self.page.locator('//div[@class="main_tool_L"]//div[text()="编辑"]')
        self.random_emoji_all = self.page.locator('//div[@class="emojiBox all"]/div')
        self.sure_in_random_emoji = self.page.locator('//div[@class="bscrmCSS-modal-footer"]').last.locator('//span[text()="确 定"]/..')
        self.notice_input = self.page.locator('//div[@class="sendContent"]//div[@id="editDiv"]')
        self.notice_text = self.page.locator('//div[@class="bscrmCSS-modal-content"]//div[@id="editDiv"]')
        self.sure_in_text_input = self.page.locator('//div[@class="bscrmCSS-modal-content"]//button/span[text()="确 定"]')
        self.add_button = self.page.locator('//div[@class="bscrmCSS-modal-content"]//div[@class="sop-upload-btn"]')
        self.upload_suc = self.page.locator('//div[@class="bscrmCSS-message"]//span[text()="上传成功~"]')
        self.link_title = self.page.get_by_placeholder('请输入链接标题')
        self.link_address = self.page.get_by_placeholder('请输入链接', exact=True)
        self.link_content = self.page.get_by_placeholder('请输入内容简介')
        self.file_name = self.page.get_by_placeholder('请输入文件名称')
        self.sure_to_submit = self.page.locator('//div[@class="btnBox"]//button/span[text()="确 定"]')
        self.search_task_name = self.page.get_by_placeholder('请输入任务名称')
        self.task_name_in_card = lambda task_name: self.page.locator(
            f'//div[@class="HighMassTexting_main_L"]//span[text()="{task_name}"]')
        self.load_tip = self.page.locator(
            '//div[@class="ant-spin ant-spin-spinning"]/span[@class="ant-spin-dot ant-spin-dot-spin"]')
        self.single_send = self.page.locator('//input[@id="singleSendFlag"]/..')
        self.regular_button = self.page.locator(
            '//div[@class="timeSeting"]//span[text()="定时发送"]/../span[@class="bscrmCSS-radio"]')
        self.time_input_button = self.page.get_by_placeholder('请选择发送时间')
        self.time_input = self.page.locator('//input[@class="bscrmCSS-calendar-input "]')
        self.sure_in_time = self.page.locator(
            '//span[@class="bscrmCSS-calendar-footer-btn"]/a[@class="bscrmCSS-calendar-ok-btn"]')

    def navigate(self):
        with allure.step('进入高级群发界面'):
            self.jump("/mantis/bscrm/highMassTexting")

    def upload(self, path, file_type):
        num = 0
        with allure.step(f'上传{file_type}'):
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

    def send_content_text(self, text):
        with allure.step('点击文本按钮'):
            self.send_content('文本').click()
            with allure.step(f'在文本编辑--文本输入框中，输入内容：{text}'):
                self.text_input.type(text)
            with allure.step(f'在文本编辑界面插入表情'):
                self.emoji_button.click()
                # self.page.wait_for_timeout(2_000)
                emoji_len = self.emoji.count()
                self.emoji_button.click()
                for i in random.sample(range(0, emoji_len), 5):
                    self.emoji_button.click()
                    self.emoji.nth(i).click()
            with allure.step('在文本编辑界面--插入员工姓名'):
                self.placeholder('插入员工姓名').click()
            with allure.step('在文本编辑界面--添加@所有人'):
                self.placeholder('@所有人').click()
            with allure.step('在文本编辑界面--添加直播链接'):
                self.placeholder('直播链接').click()
                with allure.step('在选择直播界面，点击直播时间'):
                    self.start_date.click()
                    date_start, date_end = 返回当前日期和减N天的日期(-6, '使用年月日格式')
                    self.date(date_start).click()
                    self.date(date_end).click()
                    self.live_video.click()
                    self.sure_in_choose_live_video.click()
            with allure.step('在文本编辑界面--添加营期课链接'):
                self.placeholder('营期课链接').click()
                self.xunlianying_select.click()
                self.xunlianying.click()
                self.yingqi_select.click()
                self.yingqi.click()
                self.yingqi_video.click()
                self.sure_in_choose_yingqi_video.click()
            with allure.step('在文本编辑界面--编辑随机 表情'):
                self.random_emoji_edit.click()
                emoji_len = self.random_emoji_all.count()
                for i in random.sample(range(0, emoji_len), 10):
                    self.random_emoji_all.nth(i).click()
                self.sure_in_random_emoji.click()
                self.random_emoji.click()
            with allure.step(f'在文本编辑中，点击确定按钮'):
                self.sure_in_text_input.click()

    def create_task_func(self, task_name, wechat_name, task_type, send_object_type, send_name_list='', text='',
                         picture='', video='', link: dict = '', file: dict = '', notice='', **kwargs):
        one_by_one = kwargs.get('one_by_one')
        regular = kwargs.get('regular')
        if isinstance(regular, bool) and regular:
            regular = 5
        elif isinstance(regular, int):
            regular = regular
        else:
            regular = False
        with allure.step(f'鼠标hover到新建任务按钮上，并点击{task_type}'):
            with self.page.expect_response(r'https://qaks.bjmantis.net/e-wechat/device/queryParams') as response_info:
                self.hover_with_retry(self.create_task, self.send(task_type))
                response = response_info.value
                RPA_TASK_BUG_SEND_FLAG = response.json().get('data').get('RPA_TASK_BUG_SEND_FLAG')  # 卡bug参数
        if RPA_TASK_BUG_SEND_FLAG == 'Y' and task_type != '群发公告':
            video = None
            file = None
        if task_type == '私聊群发':
            send_object = self.send_object_person
        else:
            send_object = self.send_object_group
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
                self.sure.click()
        with allure.step(f'在群发对象中，选择{send_object_type}'):
            if send_object_type == '指定群' or send_object_type == '按客户':
                self.form_radio_choose(label='群发对象', radio=send_object_type)
                with allure.step('点击选择客户/选择客户群'):
                    send_object.click()
                    for name in send_name_list:
                        with allure.step(f'在选择客户/客户群界面，输入：{name}，并按回车键'):
                            self.group_name.fill(name)
                            self.page.keyboard.press('Enter')
                    with allure.step(f'在选择客户/客户群界面，点击全选本页'):
                        self.check_all.click()
                    with allure.step(f'在选择客户/客户群界面，点击确定按钮'):
                        self.sure_in_choose_send_object.click()
            elif send_object_type == '按条件':
                self.form_radio_choose(label='群发对象', radio=send_object_type)
        if notice:
            with allure.step(f'输入群公告内容：{notice}'):
                self.notice_input.type(notice)
        if text:
            self.send_content_text(text)
        if picture:
            with allure.step('在追加内容中，点击图片按钮'):
                self.send_content('图片').click()
                self.upload(picture, '图片')
        if video:
            with allure.step('在追加内容中，点击视频按钮'):
                self.send_content('视频').click()
                self.upload(video, '视频')
        if file:
            file_name = file.get('file_name')
            file_path = file.get('file_path')
            with allure.step('在追加内容中，点击文件按钮'):
                self.send_content('文件').click()
                with allure.step(f'在上传文件界面--文件名称输入框中，输入文件名称：{file_name}'):
                    self.file_name.fill(file_name)
                self.upload(file_path, '文件')
        if link:
            with allure.step('在追加内容中，点击链接按钮'):
                self.send_content('链接').click()
                title = link['title']
                with allure.step(f'在链接标题中输入{title}'):
                    self.link_title.fill(title)
                address = link['address']
                with allure.step(f'在链接地址中输入{address}'):
                    self.link_address.fill(address)
                content = link['content']
                with allure.step(f'在内容简介中输入{content}'):
                    self.link_content.fill(content)
                self.upload(link['picture_path'], '链接图片')
        if one_by_one:
            with allure.step('在模式设置--发送模板中，勾选【指定的群单独发送】'):
                self.single_send.click()
        if regular:
            with allure.step(f'在发送类型中，点击定时发送'):
                self.regular_button.click()
            self.time_input_button.click()
            send_time = get_time(regular)
            with allure.step(f'在日期选择界面--发送时间输入框中，输入发送时间：{send_time}'):
                self.time_input.fill(send_time)
            with allure.step(f'在日期选择界面，点击确定按钮'):
                self.sure_in_time.click()
        # with allure.step(f'点击确定按钮--提交表单'):
        #     self.sure_to_submit.click()
        # expect(self.sure_to_submit).not_to_be_visible()
        # with allure.step(f'在高级群发列表--任务名称查询框中，输入任务名称：{task_name}，并按回车触发查询'):
        #     self.search_task_name.fill(task_name)
        #     self.page.keyboard.press('Enter')
        # with allure.step(f'在高级群发列表中，任务名称：【{task_name}】查询成功'):
        #     expect(self.task_name_in_card(task_name)).to_be_visible()

    # with page.expect_download() as f:
    #     page.locator("a").get_by_text("下载模板").click()
    # file_path = get_path(f"download/{time.time_ns()}.xlsx")
    # f.value.save_as(file_path)
    # page.set_input_files('//input[@type="file"]', get_path("data_module/testupload.xlsx"))
    # expect(page.get_by_text("testupload.xlsx")).to_be_visible()
