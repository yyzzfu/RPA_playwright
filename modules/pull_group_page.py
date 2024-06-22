from modules import *


class PullGroupPage(PageObject):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_task = self.page.get_by_text("新建任务")
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

        self.atuo_create_group = self.page.locator('//button[@id="autoCreateGroupFlag"]')
        self.new_group_name = self.page.get_by_placeholder('请输入群名称')
        self.code = self.page.locator('//input[@id="createGroupNameSuffix"]')
        self.fixed_kehu = self.page.locator('//div[@name="addUserGroupList"]//button')
        self.fixed_employee = self.page.locator('//div[@name="externalInList"]//button')
        self.search_employee = self.page.get_by_placeholder('请搜索')
        self.employee = lambda employee: self.page.locator(
            f'//div[@class="rember-select-modal"]//span[text()="{employee}"]/../../../..//span[@class="bscrmCSS-tree-checkbox"]')
        self.sure_in_employee = self.page.locator(
            '//div[@class="rember-modal-bottom"]/button[@class="bscrmCSS-btn bscrmCSS-btn-primary"]')
        self.members_count = self.page.locator('//input[@id="toGroupUserNum"]')
        self.group_rate = self.page.locator('//input[@id="toGroupJoinUserRate"]')

        self.sure_to_submit = self.page.locator('//div[@class="btnBox"]//button/span[text()="确 定"]')

        self.search_task_name = self.page.get_by_placeholder('请输入任务名称')
        self.task_name_in_card = lambda task_name: self.page.locator(
            f'//div[@class="HighMassTexting_main_L"]//span[text()="{task_name}"]')
        self.load_tip = self.page.locator(
            '//div[@class="ant-spin ant-spin-spinning"]/span[@class="ant-spin-dot ant-spin-dot-spin"]')
        self.group_name_exsit = lambda group_name: self.page.locator(f'//div[@class="table_groupInfo"]//div[contains(text(), "{group_name}")]')

    def navigate(self):
        self.jump("/mantis/bscrm/batchGrouping")

    def create_task_create_group(self, task_name, wechat_name_list, name_list, new_group_name, code,
                            name_fixed_list, employee, members_count, group_rate):
        self.create_task.click()
        self.task_name.fill(task_name)
        self.choose_wechat.click()
        for wechat_name in wechat_name_list:
            self.wechat(wechat_name).click()
        self.sure.click()
        self.send_object_person.click()
        for name in name_list:
            self.group_name.fill(name)
            self.page.keyboard.press('Enter')
        self.check_all.click()
        self.sure_in_choose_send_object.click()

        self.atuo_create_group.click()
        self.new_group_name.fill(new_group_name)
        self.code.fill(code)
        self.fixed_kehu.click()
        for name in name_fixed_list:
            self.group_name.fill(name)
            self.page.keyboard.press('Enter')
        self.check_all.click()
        self.sure_in_choose_send_object.click()

        self.fixed_employee.click()
        self.search_employee.fill(employee)
        self.employee(employee).click()
        self.sure_in_employee.click()
        self.members_count.fill(members_count)
        self.group_rate.fill(group_rate)
        self.sure_to_submit.click()
        expect(self.sure_to_submit).not_to_be_visible()
        self.search_task_name.fill(task_name)
        self.page.keyboard.press('Enter')
        expect(self.task_name_in_card(task_name)).to_be_visible()

    def create_task_pull_kehu(self, task_name, wechat_name_list, name_pull_list,
                              pull_group_name, members_count, group_rate):
        self.create_task.click()
        self.task_name.fill(task_name)
        self.choose_wechat.click()
        for wechat_name in wechat_name_list:
            self.wechat(wechat_name).click()
        self.sure.click()
        self.send_object_person.click()
        for name in name_pull_list:
            self.group_name.fill(name)
            self.page.keyboard.press('Enter')
        self.check_all.click()
        self.sure_in_choose_send_object.click()

        self.send_object_group.click()

        num = 0
        while True:
            try:
                self.group_name.fill(pull_group_name)
                self.page.keyboard.press('Enter')
                if self.group_name_exsit(pull_group_name).count():
                    break
            except Exception as e:
                num += 1
                if num == 5:
                    raise e
        self.check_all.click()
        self.sure_in_choose_send_object.click()
        self.members_count.fill(members_count)
        self.group_rate.fill(group_rate)
        self.sure_to_submit.click()
        expect(self.sure_to_submit).not_to_be_visible()
        self.search_task_name.fill(task_name)
        self.page.keyboard.press('Enter')
        expect(self.task_name_in_card(task_name)).to_be_visible()
