from module import *
from utils.tools import get_time


class PullGroupPage(BasePage):
    """批量拉群"""

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
        self.group_name_exsit = lambda group_name: self.page.locator(
            f'//div[@class="table_groupInfo"]//div[contains(text(), "{group_name}")]')

        self.regular_button = self.page.locator(
            '//div[@class="timeSeting"]//span[text()="单次定时"]/../span[@class="bscrmCSS-radio"]')
        self.time_input_button = self.page.get_by_placeholder('请选择发送时间')
        self.time_input = self.page.locator('//input[@class="bscrmCSS-calendar-input "]')
        self.sure_in_time = self.page.locator(
            '//span[@class="bscrmCSS-calendar-footer-btn"]/a[@class="bscrmCSS-calendar-ok-btn"]')

    def navigate(self):
        with allure.step('进入批量拉群界面'):
            self.jump("/mantis/bscrm/batchGrouping")

    def create_task_create_group(self, task_name, wechat_name_list, name_list, new_group_name, code,
                                 name_fixed_list, employee, members_count, group_rate):
        with allure.step('点击新建任务按钮'):
            self.create_task.click()
        with allure.step(f'在批量拉群编辑界面，输入任务名称：{task_name}'):
            self.task_name.fill(task_name)
        with allure.step('点击选择企微账号'):
            self.choose_wechat.click()
        for wechat_name in wechat_name_list:
            with allure.step(f'勾选企微账号：{wechat_name}'):
                self.wechat(wechat_name).click()
        with allure.step(f'在选择企微账号界面，点击确定按钮'):
            self.sure.click()
        with allure.step(f'在被邀请客户中，点击选择客户'):
            self.send_object_person.click()
        for name in name_list:
            with allure.step(f'在选择客户界面--备注中，输入客户名称：{name}，并按回车键'):
                self.group_name.fill(name)
                self.page.keyboard.press('Enter')
        with allure.step(f'在选择客户界面，点击全选本页'):
            self.check_all.click()
        with allure.step(f'在选择客户界面，点击确定按钮'):
            self.sure_in_choose_send_object.click()
        with allure.step(f'开启自动新建群聊'):
            self.atuo_create_group.click()
        with allure.step(f'输入新建群名称：{new_group_name}'):
            self.new_group_name.fill(new_group_name)
        with allure.step(f'输入编号：{code}'):
            self.code.fill(code)
        with allure.step(f'新群固定客户中，点击选择客户'):
            self.fixed_kehu.click()
        for name in name_fixed_list:
            with allure.step(f'在选择客户界面--备注中，输入客户名称：{name}，并按回车键'):
                self.group_name.fill(name)
                self.page.keyboard.press('Enter')
        with allure.step(f'在选择客户界面，点击全选本页'):
            self.check_all.click()
        with allure.step(f'在选择客户界面，点击确定按钮'):
            self.sure_in_choose_send_object.click()
        with allure.step(f'在新群固定员工中，点击添加员工'):
            self.fixed_employee.click()
        with allure.step(f'在选择员工界面--搜索框中，输入员工：{employee},并勾选该员工'):
            self.search_employee.fill(employee)
            self.employee(employee).click()
        with allure.step(f'在选择员工界面，点击确定按钮'):
            self.sure_in_employee.click()
        with allure.step(f'输入目标成员数：{members_count}'):
            self.members_count.fill(members_count)
        with allure.step(f'输入预计入群率：{group_rate}'):
            self.group_rate.fill(group_rate)
        with allure.step(f'点击确定按钮--提交表单'):
            self.sure_to_submit.click()
        with allure.step('等待确定按钮消失'):
            expect(self.sure_to_submit).not_to_be_visible()
        with allure.step(f'在批量拉群列表--任务名称查询框中，输入任务名称：{task_name}，并按回车触发查询'):
            self.search_task_name.fill(task_name)
            self.page.keyboard.press('Enter')
        with allure.step(f'在批量拉群列表中，任务名称：【{task_name}】查询成功'):
            expect(self.task_name_in_card(task_name)).to_be_visible()

    def create_task_pull_kehu(self, task_name, wechat_name_list, name_pull_list,
                              pull_group_name, members_count, group_rate, **kwargs):
        regular = kwargs.get('regular')
        if isinstance(regular, bool) and regular:
            regular = 5
        elif isinstance(regular, int):
            regular = regular

        with allure.step('点击新建任务按钮'):
            self.create_task.click()
        with allure.step(f'在批量拉群编辑界面，输入任务名称：{task_name}'):
            self.task_name.fill(task_name)
        with allure.step('点击选择企微账号'):
            self.choose_wechat.click()
        for wechat_name in wechat_name_list:
            with allure.step(f'勾选企微账号：{wechat_name}'):
                self.wechat(wechat_name).click()
        with allure.step(f'在选择企微账号界面，点击确定按钮'):
            self.sure.click()
        with allure.step(f'在被邀请客户中，点击选择客户'):
            self.send_object_person.click()
        for name in name_pull_list:
            with allure.step(f'在选择客户界面--备注中，输入客户名称：{name}，并按回车键'):
                self.group_name.fill(name)
                self.page.keyboard.press('Enter')
        with allure.step(f'在选择客户界面，点击全选本页'):
            self.check_all.click()
        with allure.step(f'在选择客户界面，点击确定按钮'):
            self.sure_in_choose_send_object.click()
        with allure.step(f'目标群聊--选择现有群中，点击选择客户群'):
            self.send_object_group.click()

        num = 0
        while True:
            try:
                with allure.step(f'在选择客户群界面--群名称中，输入群名称：{pull_group_name}，并按回车键'):
                    self.group_name.fill(pull_group_name)
                    self.page.keyboard.press('Enter')
                if self.group_name_exsit(pull_group_name).count():
                    break
                raise Exception
            except Exception as e:
                num += 1
                if num == 5:
                    raise e
        with allure.step(f'在选择客户群界面，点击全选本页'):
            self.check_all.click()
        with allure.step(f'在选择客户群界面，点击确定按钮'):
            self.sure_in_choose_send_object.click()
        with allure.step(f'输入目标成员数：{members_count}'):
            self.members_count.fill(members_count)
        with allure.step(f'输入预计入群率：{group_rate}'):
            self.group_rate.fill(group_rate)
        if regular:
            with allure.step(f'在发送类型中，点击单次定时'):
                self.regular_button.click()
            self.time_input_button.click()
            send_time = get_time(regular)
            with allure.step(f'在日期选择界面--发送时间输入框中，输入发送时间：{send_time}'):
                self.time_input.fill(send_time)
            with allure.step(f'在日期选择界面，点击确定按钮'):
                self.sure_in_time.click()
        with allure.step(f'点击确定按钮--提交表单'):
            self.sure_to_submit.click()
        with allure.step('等待确定按钮消失'):
            expect(self.sure_to_submit).not_to_be_visible()
        with allure.step(f'在批量拉群列表--任务名称查询框中，输入任务名称：{task_name}，并按回车触发查询'):
            self.search_task_name.fill(task_name)
            self.page.keyboard.press('Enter')
        with allure.step(f'在批量拉群列表中，任务名称：【{task_name}】查询成功'):
          expect(self.task_name_in_card(task_name)).to_be_visible()
