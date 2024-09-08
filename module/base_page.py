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
        return Table(self.page, only_text, table_index)

    def jump(self, path: str = None):
        if path[0] != "/":
            path = f"/{path}"
        self.page.goto(path, wait_until='networkidle')

    def form_input_fill(self, label: str, content: str, form_only_locator: Locator = None, timeout: float = None):
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator("input,textarea").locator(
                "visible=true").last.fill(content, timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).locator("input,textarea").locator("visible=true").last.fill(content,
                                                                                                               timeout=timeout)

    def form_select_choose(self, label: str, option: str, form_only_locator: Locator = None, timeout: float = None):
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
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator("label").locator(
                "visible=true").filter(has_text=radio).locator("input").check(timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).locator("label").locator("visible=true").filter(
                has_text=radio).locator("input").check(timeout=timeout)

    def form_switch(self, label: str, swith_status: str, form_only_locator: Locator = None, timeout: float = None):
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
        if form_only_locator:
            data_locator = form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label))
        else:
            data_locator = self.locators.表单项中包含操作元素的最上级div(label)
        data_locator.locator("input").click(timeout=timeout)
        data_locator.locator("input").filter(has=self.page.locator('.bscrmCSS-calendar-input ').fill(get_time(time_minute), timeout=timeout))
        data_locator.locator("input").filter(has=self.page.locator('.bscrmCSS-calendar-input ').blur(timeout=timeout))  # 失焦

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
        for label, content in kwargs.items():
            if not content:
                continue
            elif self.locators.表单项中包含操作元素的最上级div(label).locator(".bscrmCSS-input").count():
                self.form_input_fill(label=label, content=content, form_only_locator=form_only_locator, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(label).locator(".ant-select-selector").count():
                self.form_select_choose(label=label, option=content, form_only_locator=form_only_locator, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(label).locator(".bscrmCSS-radio-input").count():
                self.form_radio_choose(label=label, radio=content, form_only_locator=form_only_locator, timeout=timeout)
            elif self.locators.表单项中包含操作元素的最上级div(label).get_by_role("switch").count():
                self.form_switch(label=label, swith_status=content, form_only_locator=form_only_locator, timeout=timeout)
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
