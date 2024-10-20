import time

from module import *
from module.locators import Locators
from module.table import Table
from utils.tools import get_time


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
