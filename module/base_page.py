import time

from module import *
from module.locators import Locators
from module.table import Table
from utils.tools import get_time
from utils.tools import 返回当前日期和减N天的日期, 将日期中的01日替换为1日



class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = Locators(self.page)

    def navigate(self):
        self.jump()

    def table(self, only_text: str = '', table_index: int = -1):
        """
        :param only_text: 唯一文字
        :param table_index: 表格序号
        :return:
        """
        return Table(self.page, only_text, table_index)

    def jump(self, path: str = None):
        if path[0] != "/":
            path = f"/{path}"
        self.page.goto(path, wait_until='networkidle')

    def hover_with_retry(self, hover_object: Locator, click_object: Locator, first_step="hover", second_step="click",
                         timeout=30_000):
        """
        如果hover操作失败，会自动重试
        :param hover_object: hover对象
        :param click_object: 下一步点击对象
        :param first_step: 第一步动作
        :param second_step: 第二步动作
        :param timeout:
        :return:
        """
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout / 1000:
                pytest.fail(f"hover重试{hover_object.__str__()}在{timeout/1000}秒内未成功")
            try:
                self.page.mouse.move(x=1, y=1)
                self.page.wait_for_timeout(1_000)
                if first_step == "hover":
                    hover_object.last.hover()
                else:
                    hover_object.last.click()
                if second_step == "click":
                    click_object.last.click(timeout=3000)
                else:
                    click_object.last.wait_for(state="visible", timeout=3000)
                break
            except:
                continue

    def form_input_fill(self, label: str, content: str, form_only_locator: Locator = None, timeout: float = None):
        """
        表单文本框填写
        :param label: 表单项名称
        :param content: 需要填写的文本
        :param form_only_locator: 表单最上层定位
        :param timeout: 超时时间（秒）
        :return:
        """
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator("input,textarea").locator(
                "visible=true").last.fill(content, timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).locator("input,textarea").locator("visible=true").last.fill(content,
                                                                                                               timeout=timeout)

    def form_select_choose(self, label: str, option: str, form_only_locator: Locator = None, timeout: float = None):
        """
        表单下拉框选择
        :param label: 表单项名称
        :param option:需要选择的项
        :param form_only_locator:表单最上层定位
        :param timeout:超时时间（秒）
        :return:
        """
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator("visible=true").click(
                timeout=timeout)
            if form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator(
                    '//input[@type="search"]').count():
                form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator(
                    '//input[@type="search"]').fill(option, timeout=timeout)
            self.page.locator(".ant-select-dropdown").locator("visible=true").get_by_text(option).click(timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).locator("visible=true").click(timeout=timeout)
            if self.locators.表单项中包含操作元素的最上级div(label).locator('//input[@type="search"]').count():
                self.locators.表单项中包含操作元素的最上级div(label).locator('//input[@type="search"]').fill(option, timeout=timeout)
            self.page.locator(".ant-select-dropdown").locator("visible=true").get_by_text(option).click(timeout=timeout)
        expect(self.page.locator(".ant-select-dropdown")).to_be_hidden(timeout=timeout)

    def form_radio_choose(self, label: str, radio: str, form_only_locator: Locator = None, timeout: float = None):
        """
        表单radio选择
        :param label: 表单项名称
        :param radio:需要选择的项
        :param form_only_locator:表单最上层定位
        :param timeout:超时时间（秒）
        :return:
        """
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator("label").locator(
                "visible=true").filter(has_text=radio).locator("input").check(timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).locator("label").locator("visible=true").filter(
                has_text=radio).locator("input").check(timeout=timeout)

    def form_switch(self, label: str, swith_status: str, form_only_locator: Locator = None, timeout: float = None):
        """
        表单switch开关操作
        :param label: 表单项名称
        :param swith_status:开关状态
        :param form_only_locator:表单最上层定位
        :param timeout:超时时间（秒）
        :return:
        """
        if "开" in swith_status or "是" in swith_status:
            swith_status = True
        else:
            swith_status = False
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).get_by_role("switch").set_checked(
                swith_status, timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).get_by_role("switch").set_checked(swith_status, timeout=timeout)

    def form_date(self, label: str, time_minute: str, form_only_locator: Locator = None, timeout: float = None):
        """
        表单日期、时间操作
        :param label: 表单项名称
        :param time_minute:时间
        :param form_only_locator:表单最上层定位
        :param timeout:超时时间（秒）
        :return:
        """
        if form_only_locator:
            data_locator = form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label))
        else:
            data_locator = self.locators.表单项中包含操作元素的最上级div(label)
        data_locator.locator("input").click(timeout=timeout)
        data_locator.locator("input").filter(
            has=self.page.locator('.bscrmCSS-calendar-input ').fill(get_time(time_minute), timeout=timeout))
        data_locator.locator("input").filter(
            has=self.page.locator('.bscrmCSS-calendar-input ').blur(timeout=timeout))  # 失焦

        # date_list = date.split(",")
        # for index, 单日期 in enumerate(date_list):
        #     try:
        #         int(单日期)
        #         格式化后的日期 = 返回当前时间xxxx_xx_xx加N天(int(单日期))
        #     except:
        #         格式化后的日期 = 单日期
        # data_locator.locator("input").filter(has=self.page.locator('.bscrmCSS-calendar-input ').nth(index).fill(格式化后的日期, timeout=timeout))
        # data_locator.locator("input").nth(index).blur(timeout=timeout)  # 失焦

    def fill_form(self, form_only_locator: Locator = None, timeout=None, **kwargs):
        """
        快捷操作填写表单
        :param form_only_locator: 表单最上层定位
        :param timeout:超时时间（秒）
        :param kwargs:
        :return:
        """
        for label, content in kwargs.items():
            if not content:
                continue
            elif self.locators.表单项中包含操作元素的最上级div(label).locator(".bscrmCSS-input").count():
                self.form_input_fill(label=label, content=content, form_only_locator=form_only_locator, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(label).locator(".ant-select-selector").count():
                self.form_select_choose(label=label, option=content, form_only_locator=form_only_locator,
                                        timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(label).locator(".bscrmCSS-radio-input").count():
                self.form_radio_choose(label=label, radio=content, form_only_locator=form_only_locator, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(label).get_by_role("switch").count():
                self.form_switch(label=label, swith_status=content, form_only_locator=form_only_locator,
                                 timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(label).locator(".bscrmCSS-calendar-picker-input").count():
                self.form_date(label=label, time_minute=content, form_only_locator=form_only_locator, timeout=timeout)
            else:
                pytest.fail(f"不支持的快捷表单填写:\n{label}:{content}")

    def 快捷操作_填写表单_增加根据数据类确定唯一表单版(self, 表单最上层定位: Locator = None, timeout=None, **kwargs):
        页面上已有的表单项列表 = []
        已经有唯一表单项 = False
        if 表单最上层定位:
            处理后的表单最上层定位 = 表单最上层定位
        else:
            for index, 表单项 in enumerate(kwargs.keys()):
                if index == 0:
                    try:
                        self.locators.表单项中包含操作元素的最上级div(表单项).last.wait_for(timeout=timeout)
                    except:
                        pass

                if self.locators.表单项中包含操作元素的最上级div(表单项).count() == 0:
                    continue
                else:
                    if self.locators.表单项中包含操作元素的最上级div(表单项).count() == 1:
                        已经有唯一表单项 = True
                    页面上已有的表单项列表.append(self.locators.表单项中包含操作元素的最上级div(表单项))
                if 已经有唯一表单项 and len(页面上已有的表单项列表) >= 2:
                    break

            包含可见表单项的loc = self.page.locator("*")
            for 已有表单项_loc in 页面上已有的表单项列表:
                包含可见表单项的loc = 包含可见表单项的loc.filter(has=已有表单项_loc)
            if 已经有唯一表单项:
                处理后的表单最上层定位 = 包含可见表单项的loc.last
            else:
                处理后的表单最上层定位 = min(包含可见表单项的loc.all(), key=lambda loc: len(loc.text_content()))

        for 表单项, 内容 in kwargs.items():
            if not 内容:
                continue
            if self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-input").count():
                self.表单_文本框填写(表单项名称=表单项, 需要填写的文本=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-select-selector").count():
                self.表单_下拉框选择(表单项名称=表单项, 需要选择的项=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-radio-group").count():
                self.表单_radio选择(表单项名称=表单项, 需要选择的项=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).get_by_role("switch").count():
                self.表单_switch开关(表单项名称=表单项, 开关状态=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(表单项).locator(".ant-picker").count():
                self.表单_日期(表单项名称=表单项, 日期=内容, 表单最上层定位=处理后的表单最上层定位, timeout=timeout)
            else:
                pytest.fail(f"不支持的快捷表单填写:\n{表单项}:{内容}")

    @allure.step("重试")
    def retry(self, *args, retry_count=10):
        """
        重试一系列步骤
        @param args:
        1. 第一个传的是子步骤的指针,比如locator.click, locator.hover
        2. 如果只传子步骤指针,则默认执行时的timeout为3_000
        3. 如果需要传参,则需要使用(子步骤指针, 位置参数1, 位置参数2, {"命名参数名称1": 命名参数值1, "命名参数名称2": 命名参数值2})
        @param retry_count: 重试次数
        @return:
        """
        for _ in range(retry_count):
            try:
                for arg in args:
                    if isinstance(arg, tuple):
                        with allure.step(f"{arg[0].__name__} 参数:{arg[1:]}"):
                            func = arg[0]
                            param = arg[1:]
                            named_params = {}
                            positional_params = []
                            for in_param in param:
                                if isinstance(in_param, dict):
                                    named_params.update(in_param)
                                else:
                                    positional_params.append(in_param)
                            func(*positional_params, **named_params)
                    else:
                        with allure.step(arg.__name__):
                            arg(timeout=3000)
                break
            except Exception as e:
                if _ == retry_count - 1:
                    print(f"已经重试{retry_count}次，但仍然失败，错误信息：", e)
                    raise e
        # for _ in range(重试次数):
        #     try:å
        #         for arg in args:
        #             if isinstance(arg, tuple):
        #                 with allure.step(f"{arg[0].__name__} 参数:{arg[1:]}"):
        #                     f = arg[0]
        #                     param = arg[1:]
        #                     f(*param)
        #             else:
        #                 with allure.step(arg.__name__):
        #                     arg(timeout=3000)
        #         break
        #     except Exception as e:
        #         if _ == 重试次数 - 1:
        #             print(f"已经重试{重试次数}次，但仍然失败，错误信息：", e)
        #             raise e

    def choose_wecome(self, wechat_name):
        choose_wechat = self.page.locator("//button/span[text()='选择企微账号']")
        wechat = lambda wechat_name1: self.page.locator(
            f'//table//td[text()="{wechat_name1}"]/../td[@class="bscrmCSS-table-selection-column"]')

        with allure.step('点击选择企微账号'):
            choose_wechat.click()
            if isinstance(wechat_name, list):
                for name in wechat_name:
                    with allure.step(f'在选择企微账号界面，选择企微账号：{name}'):
                        wechat(name).click()
            else:
                with allure.step(f'在选择企微账号界面，选择企微账号：{wechat_name}'):
                    wechat(wechat_name).click()
            with allure.step('在选择企微账号界面，点击确定按钮'):
                self.locators.button('确定').click()

    def choose_send_object(self, send_object_type, send_name_list):
        send_object = self.page.locator(f"//button/span[contains(text(), '选择客户')]")
        group_name = self.page.get_by_placeholder('可输入多个，按回车或后面的加号')
        check_all = self.page.get_by_text('全选所有')

        with allure.step(f'在群发对象中，选择{send_object_type}'):
            if send_object_type == '指定群' or send_object_type == '按客户':
                self.form_radio_choose(label='群发对象', radio=send_object_type)
                with allure.step('点击选择客户/选择客户群'):
                    send_object.click()
                    for name in send_name_list:
                        with allure.step(f'在选择客户/客户群界面，输入：{name}，并按回车键'):
                            group_name.fill(name)
                            self.page.keyboard.press('Enter')
                    with allure.step(f'在选择客户/客户群界面，点击全选本页'):
                        check_all.click()
                    with allure.step(f'在选择客户/客户群界面，点击确定按钮'):
                        self.locators.button('确定').click()
            elif send_object_type == '按条件':
                self.form_radio_choose(label='群发对象', radio=send_object_type)

    def upload(self, path, file_type):
        add_button = self.page.locator('//div[@class="bscrmCSS-modal-content"]//div[@class="sop-upload-btn"]')
        upload_suc = self.page.locator('//div[@class="bscrmCSS-message"]//span[text()="上传成功~"]')

        num = 0
        with allure.step(f'上传{file_type}'):
            while True:
                try:
                    self.page.wait_for_timeout(1_000)
                    with self.page.expect_file_chooser() as f:
                        add_button.click()
                        break
                except Exception as e:
                    num += 1
                    if num == 3:
                        raise e
            f.value.set_files(path)
            expect(upload_suc).to_be_visible()
            expect(add_button).not_to_be_visible()
        if file_type != '链接图片':
            with allure.step('在上传界面，点击确定按钮'):
                self.locators.button('确定').click()
        # with page.expect_download() as f:
        #     page.locator("a").get_by_text("下载模板").click()
        # file_path = get_path(f"download/{time.time_ns()}.xlsx")
        # f.value.save_as(file_path)
        # page.set_input_files('//input[@type="file"]', get_path("data_module/testupload.xlsx"))
        # expect(page.get_by_text("testupload.xlsx")).to_be_visible()

    def add_emoji(self, num):
        emoji_button = self.page.locator('//img[@class="emoji_btn"]')  # 表情按钮
        emoji = self.page.locator('//div[@class="emojiBox"]/div')

        with allure.step(f'插入{num}个表情'):
            emoji_len = emoji.count()
            for i in random.sample(range(0, emoji_len), num):
                emoji_button.click()
                # self.page.wait_for_timeout(500)
                emoji.nth(i).click()

    def add_live_link(self, click_button=True):
        placeholder = lambda placeholder1: self.page.locator(f'//div[@class="main_tool_L"]/span[text()="{placeholder1}"]').last  # 占位符按钮
        start_date = self.page.locator('//input[@placeholder="开始日期"]')
        date = lambda date1: self.page.locator(
            f'//div[@class="bscrmCSS-calendar-range-part bscrmCSS-calendar-range-left"]//td[@title="{date1}"]')
        live_video_tr = self.page.locator('//tbody[@class="bscrmCSS-table-tbody"]').last.locator('tr')
        live_video_radio = live_video_tr.locator('td').nth(0)
        live_video_info = live_video_tr.locator('td').nth(1)

        with allure.step('添加直播链接'):
            if click_button:
                placeholder('直播链接').click()
            with allure.step('在选择直播界面，点击直播时间'):
                start_date.click()
                date_start, date_end = 返回当前日期和减N天的日期(-4, '使用年月日格式')
                date_start = 将日期中的01日替换为1日(date_start)
                date_end = 将日期中的01日替换为1日(date_end)
                date(date_start).click()
                date(date_end).click()
                live_video_info = live_video_info.text_content()
            with allure.step(f'在选择直播界面，选择直播课：{live_video_info}'):
                live_video_radio.click()
            with allure.step(f'在选择直播界面，点击确定按钮'):
                self.locators.button('确定').click()

    def add_yingqi_link(self, click_button=True, sop=False):
        placeholder = lambda placeholder1: self.page.locator(f'//div[@class="main_tool_L"]/span[text()="{placeholder1}"]').last  # 占位符按钮
        xunlianying_select = self.page.locator('//div[text()="请选择训练营"]')
        xunlianying = self.page.locator(
            '//ul[@class="bscrmCSS-select-dropdown-menu  bscrmCSS-select-dropdown-menu-root bscrmCSS-select-dropdown-menu-vertical"]/li').first
        yingqi_select = self.page.locator('//div[text()="请选择营期"]')
        yingqi = self.page.locator(
            '//ul[@class="bscrmCSS-select-dropdown-menu  bscrmCSS-select-dropdown-menu-root bscrmCSS-select-dropdown-menu-vertical"]').last.locator(
            '//li').first
        yingqi_video_div = self.page.locator('//div[@class="ReactVirtualized__Grid__innerScrollContainer"]//div').first
        yingqi_video_info = yingqi_video_div.locator('//span[@class="name"]')
        with allure.step('添加营期课链接'):
            if click_button:
                placeholder('营期课链接').click()
            if not sop:
                xunlianying_select.click()
                xunlianying_name = xunlianying.text_content()
                xunlianying.click()
                yingqi_name = yingqi.text_content()
                yingqi_select.click()
                yingqi.click()
                yingqi_video_name = yingqi_video_info.text_content()
                video_info = xunlianying_name + '--' + yingqi_name + '--' + yingqi_video_name
            else:
                video_info = yingqi_video_info.text_content()
            with allure.step(f'在选择营期课界面，选择课程：{video_info}'):
                yingqi_video_info.click()
            self.locators.button('确定').click()

    def add_random_emoji(self, num):
        random_emoji = self.page.locator('//div[@class="main_tool_L"]//div[text()="随机表情"]')
        random_emoji_edit = self.page.locator('//div[@class="main_tool_L"]//div[text()="编辑"]')
        random_emoji_all = self.page.locator('//div[@class="emojiBox all"]/div')

        with allure.step('编辑随机、选择随机表情'):
            random_emoji_edit.click()
            emoji_len = random_emoji_all.count()
            for i in random.sample(range(0, emoji_len), num):
                random_emoji_all.nth(i).click()
            self.locators.button('确定').click()
            random_emoji.click()

    def add_picture(self, picture, send_content=None):
        if send_content:
            send_content = send_content
        else:
            send_content = self.page.locator(f'//div[@class="sendContent"]//span[text()="图片"]')

        with allure.step('点击图片按钮'):
            send_content.click()
            self.upload(picture, '图片')

    def add_video(self, video, send_content=None):
        if send_content:
            send_content = send_content
        else:
            send_content = self.page.locator(f'//div[@class="sendContent"]//span[text()="视频"]')
        with allure.step('点击视频按钮'):
            send_content.click()
            self.upload(video, '视频')

    def add_file(self, file, send_content=None):
        if send_content:
            send_content = send_content
        else:
            send_content = self.page.locator(f'//div[@class="sendContent"]//span[text()="文件"]')
        file_name_l = self.page.get_by_placeholder('请输入文件名称')

        file_name = file.get('file_name')
        file_path = file.get('file_path')
        with allure.step('点击文件按钮'):
            send_content.click()
            with allure.step(f'在上传文件界面--文件名称输入框中，输入文件名称：{file_name}'):
                file_name_l.fill(file_name)
            self.upload(file_path, '文件')

    def add_link(self, link, send_content=None, sop=False):
        link_type = ['指定链接', '营期课链接', '直播课链接']
        if send_content:
            send_content = send_content
        else:
            send_content = self.page.locator(f'//div[@class="sendContent"]//span[text()="链接"]').last
        choose_class_button = self.page.locator('//button[@id="shareList"]')
        link_title = self.page.get_by_placeholder('请输入链接标题')
        link_address = self.page.get_by_placeholder('请输入链接', exact=True)
        link_content = self.page.get_by_placeholder('请输入内容简介')

        for i in link_type:
            with allure.step('点击链接按钮'):
                send_content.click()

                title = i + link['title']
                with allure.step(f'在链接标题中输入{title}'):
                    link_title.fill(title)
                if i == '指定链接':
                    address = link['address']
                    with allure.step(f'在链接地址中输入{address}'):
                        link_address.fill(address)
                elif i == '营期课链接':
                    self.form_radio_choose('链接类型', '营期课链接')
                    choose_class_button.click()
                    self.add_yingqi_link(False, sop=sop)
                elif i == '直播课链接':
                    self.form_radio_choose('链接类型', '直播课链接')
                    choose_class_button.click()
                    self.add_live_link(False)
                content = i + link['content']
                with allure.step(f'在内容简介中输入{content}'):
                    link_content.fill(content)
                self.upload(link['picture_path'], '链接图片')
                self.locators.button('确定').click()

    def add_mini_program(self, send_content=None):
        if send_content:
            send_content = send_content
        else:
            send_content = self.page.locator(f'//div[@class="sendContent"]//span[text()="小程序"]').last
        choose_sucai = self.page.locator('//div[@class="bscrmCSS-modal-content"]//span[text()="选择素材"]/..')
        sucai_div = self.page.locator('//div[@class="list-data-container"]/div').first
        sucai_input = sucai_div.locator('input')
        sucai_title = sucai_div.locator('//div[@class="top-title"]')
        with allure.step('点击小程序按钮'):
            send_content.click()
            with allure.step(f'在小程序素材选择界面，点击选择素材按钮'):
                choose_sucai.click()
                sucai_title = sucai_title.text_content()
            with allure.step(f'点击素材:{sucai_title}'):
                sucai_input.click()
                self.locators.button('保存').click()
                self.locators.button('确定').click()

    def regular_send(self, regular):
        regular_button = self.page.locator(
            '//div[@class="timeSeting"]//span[text()="定时发送"]/../span[@class="bscrmCSS-radio"]')
        time_input_button = self.page.get_by_placeholder('请选择发送时间')
        time_input = self.page.locator('//input[@class="bscrmCSS-calendar-input "]')
        sure_in_time = self.page.locator(
            '//span[@class="bscrmCSS-calendar-footer-btn"]/a[@class="bscrmCSS-calendar-ok-btn"]')

        with allure.step(f'在发送类型中，点击定时发送'):
            regular_button.click()
        time_input_button.click()
        send_time = get_time(regular)
        with allure.step(f'在日期选择界面--发送时间输入框中，输入发送时间：{send_time}'):
            time_input.fill(send_time)
        with allure.step(f'在日期选择界面，点击确定按钮'):
            sure_in_time.click()
