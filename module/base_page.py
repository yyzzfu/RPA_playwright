from playwright.sync_api import Page, Locator, expect

from module.locators import Locators


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = Locators(self.page)

    def navigate(self):
        self.jump()

    def jump(self, path: str = None):
        if path[0] != "/":
            path = f"/{path}"
        self.page.goto(path, wait_until='networkidle')

    def form_input_fill(self, label: str, content: str, form_only_locator: Locator = None, timeout: float = None):
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator("input,textarea").locator("visible=true").last.fill(content, timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).locator("input,textarea").locator("visible=true").last.fill(content, timeout=timeout)

    def form_select_choose(self, label: str, option: str, form_only_locator: Locator = None, timeout: float = None):
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator("visible=true").click(timeout=timeout)
            if form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator('//input[@type="search"]').count():
                label.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator('//input[@type="search"]').fill(option, timeout=timeout)
            self.page.locator(".ant-select-dropdown").locator("visible=true").get_by_text(option).click(timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).locator("visible=true").click(timeout=timeout)
            if self.locators.表单项中包含操作元素的最上级div(label).locator('//input[@type="search"]').count():
                self.locators.表单项中包含操作元素的最上级div(label).locator('//input[@type="search"]').fill(option, timeout=timeout)
            self.page.locator(".ant-select-dropdown").locator("visible=true").get_by_text(option).click(timeout=timeout)
        expect(self.page.locator(".ant-select-dropdown")).to_be_hidden(timeout=timeout)

    def form_radio_choose(self, label: str, radio: str, form_only_locator: Locator = None, timeout: float = None):
        if form_only_locator:
            form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).locator("label").locator("visible=true").filter(has_text=radio).locator("input").check(timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(label).locator("label").locator("visible=true").filter(has_text=radio).locator("input").check(timeout=timeout)

    # def form_switch(self, label: str, swith_status: str, form_only_locator: Locator = None, timeout: float = None):
    #     if "开" in swith_status or "是" in swith_status:
    #         swith_status = True
    #     else:
    #         swith_status = False
    #     if form_only_locator:
    #         form_only_locator.locator(self.locators.表单项中包含操作元素的最上级div(label)).get_by_role("switch").set_checked(swith_status, timeout=timeout)
    #     else:
    #         self.locators.表单项中包含操作元素的最上级div(label).get_by_role("switch").set_checked(swith_status, timeout=timeout)
