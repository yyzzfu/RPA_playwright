from module import *
from utils.tools import get_time, get_days


class TrainCampPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.train_camp_search = self.page.get_by_placeholder('请输入训练营名称')
        self.train_camp = lambda train_camp: self.page.locator('//div[@class="train-list"]//div[@class="name"]').filter(has_text=train_camp)
        self.camp = lambda camp: self.page.locator('//tbody[@class="bscrmCSS-table-tbody"]').nth(1).locator('button').filter(has_text=camp)
        self.sop = self.page.locator('//button').filter(has_text='智能助理SOP')
        self.the_day = lambda day: self.page.locator(f'//div[@class="assistant-sop-config-main-body-left"]//input[@value={day}]/../..')
        self.create_task = self.page.get_by_text("新增任务")
        self.execute_time = self.page.get_by_placeholder('请选择时间').last
        self.send_content = lambda content_type: self.page.locator('//div[@class="sopTaskContent_footer"]//span').filter(has_text=content_type).last
        self.placeholder = lambda placeholder: self.page.locator(f'//div[@class="main_tool_L"]/span[text()="{placeholder}"]')  # 占位符按钮
        self.start_date = self.page.get_by_placeholder('请选择日期')
        self.class_status = lambda class_status: self.page.locator('//label').locator('span').filter(has_text=class_status)
        self.the_class = self.page.locator('//div[@class="bscrmCSS-drawer-body"]//span[text()="指定课节"]/..')
        self.relevant_class = self.page.locator('//div[@class="bscrmCSS-drawer-body"]//span[text()="关联课节"]/..')
        self.robot_select = self.page.locator('//div[@class="bscrmCSS-select-selection__placeholder"]').filter(has_text='请选择语音机器人')
        self.robot_select_option = lambda robot: self.page.locator('//ul[@role="listbox"]/li').filter(has_text=robot)
        self.connect_button = self.page.locator('//button[@id="bootConnectFlag"]')
        self.not_connect_button = self.page.locator('//button[@id="bootNotConnectFlag"]')

        self.sure = self.page.locator('//div[@class="bscrmCSS-modal-content"]//button/span[text()="确 定"]')
        self.text_input = self.page.locator('//div[@id="editDiv"]').last
        self.notice_input = self.page.locator('//div[@class="TextModal_main"]//div[@id="editDiv"]')
        self.sure_in_text_input = self.page.locator('//div[@class="bscrmCSS-modal-content"]//button/span[text()="确 定"]')
        self.add_button = self.page.locator('//div[@class="bscrmCSS-modal-content"]//div[@class="sop-upload-btn"]')
        self.sure_to_submit = self.page.locator('//div[@class="btnBox"]//button/span[text()="确 定"]')
        self.single_send = self.page.locator('//input[@id="singleSendFlag"]/..')
        self.suc_msg = self.page.get_by_text('保存成功')

    def navigate(self):
        with allure.step('进入训练营界面'):
            self.jump("/mantis/bscrm/customerManagement/trainingCamp/trainCamp")

    def create_task_func(self, train_camp, camp, task_type_1, task_type_2='', text='', picture='',
                         video='', link: dict='', file: dict='', notice='', mini_program='',
                         one_by_one='', send_object_type='', class_status='', robot='',
                         connect_content=False, not_connect_content=False, **kwargs):

        with allure.step(f'训练营查询输入框中输入名称：{train_camp}'):
            self.train_camp_search.fill(train_camp)
            self.page.keyboard.press('Enter')
        with allure.step(f'点击训练营：{train_camp}'):
            self.train_camp(train_camp).click()
        with allure.step(f'点击营期：{camp}'):
            self.camp(camp).click()
        with allure.step(f'点击智能助理SOP'):
            self.sop.click()
        start_date = ''
        for i in range(10):
            self.page.wait_for_timeout(1_000)
            start_date = self.start_date.get_attribute('value')
            if not start_date:
                continue
            else:
                break
        day = str(get_days(start_date))
        with allure.step(f'点击第{day}天'):
            if not self.the_day(day).is_visible(timeout=10_000):
                with allure.step(f'点击新建一天按钮'):
                    self.locators.button('新建一天').click()
            self.the_day(day).click()
        with allure.step(f'点击新增任务按钮'):
            self.create_task.click()
        with allure.step(f'选择任务大类：{task_type_1}'):
            self.form_radio_choose('任务大类', task_type_1)
        if task_type_2:
            with allure.step(f'选择任务小类：{task_type_2}'):
                self.form_radio_choose('任务小类', task_type_2)
        else:
            self.relevant_class.click()
            self.add_yingqi_link(click_button=False, sop=True)
            self.robot_select.click()
            self.robot_select_option(robot).click()
        if send_object_type:
            with allure.step(f'选择发送对象：{send_object_type}'):
                self.form_radio_choose('发送对象', send_object_type)
                if send_object_type == '按到课':
                    with allure.step('点击指定课节按钮'):
                        self.the_class.click()
                        self.add_yingqi_link(click_button=False, sop=True)
                    with allure.step(f'选择到课状态：{class_status}'):
                        self.class_status(class_status).click()
        if notice:
            with allure.step(f'输入群公告内容：{notice}'):
                self.notice_input.type(notice)
            self.add_live_link()
            self.add_yingqi_link(sop=True)
        if text and task_type_1 != '智能语音':
            with allure.step(f'点击文本按钮'):
                self.send_content('文本').click()
                self.text_input.fill(text)
                self.add_emoji(5)
                if task_type_1 == '高级群发':
                    self.placeholder('插入员工姓名').click()
                    if task_type_2 in ['群聊群发', '群发公告']:
                        self.placeholder('@所有人').click()
                    self.add_random_emoji(10)
                self.add_live_link()
                self.add_yingqi_link(sop=True)
                self.locators.button('确定').click()
        if picture:
            self.add_picture(picture, self.send_content('图片'))
        if video:
            self.add_video(video, self.send_content('视频'))
        if file:
            self.add_file(file, self.send_content('文件'))
        if link and task_type_1 != '智能语音':
            self.add_link(link, self.send_content('链接'), sop=True)
        if mini_program and task_type_1 != '智能语音':
            self.add_mini_program(self.send_content('小程序'))
        if one_by_one:
            with allure.step('在发送模式中，勾选【指定的群单独发送】'):
                self.single_send.click()
        execute_time = get_time(7, '时分')
        if connect_content or not_connect_content:
            if connect_content:
                with allure.step(f'开启--接通后追发内容'):
                    self.connect_button.click()
                if text:
                    with allure.step(f'点击文本按钮'):
                        self.send_content('文本').click()
                        self.text_input.fill(text+'接通后追发内容')
                        self.add_emoji(1)
                        self.placeholder('插入员工姓名').click()
                        self.add_live_link()
                        self.add_yingqi_link(sop=True)
                        self.add_random_emoji(10)
                        self.locators.button('确定').click()
                if link:
                    self.add_link(link, self.send_content('链接'), sop=True)
                if mini_program:
                    self.add_mini_program(self.send_content('小程序'))
            if not_connect_content:
                with allure.step(f'开启--未接通追发内容'):
                    self.not_connect_button.click()
                    if text:
                        with allure.step(f'点击文本按钮'):
                            self.send_content('文本').click()
                            self.text_input.fill(text+'未接通追发内容')
                            self.add_emoji(1)
                            self.placeholder('插入员工姓名').click()
                            self.add_live_link()
                            self.add_yingqi_link(sop=True)
                            self.add_random_emoji(10)
                            self.locators.button('确定').click()
                    if link:
                        self.add_link(link, self.send_content('链接'), sop=True)
                    if mini_program:
                        self.add_mini_program(self.send_content('小程序'))
        with allure.step(f'选择执行时间：{execute_time}'):
            self.execute_time.click()
            self.execute_time.fill(execute_time)
            self.page.mouse.click(1, 1)
        with allure.step(f'点击保存按钮--提交表单'):
            self.locators.button('保存').click()
        expect(self.suc_msg).to_be_visible()
