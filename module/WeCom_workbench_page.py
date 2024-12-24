from module import *
from module.base_page import BasePage


class WeComWorkbenchPage(BasePage):
    """企微工作台页面"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.all = self.page.locator('//span[@class="imgAll"]')
        self.search_input_l = self.page.locator('//div[@class="ChatListMain"]//input')
        self.search_button_l = self.page.locator('//div[@class="dialogueMain"]/div[@class="searchBox"]//button')
        # 搜索列表中的会话
        self.search_result_chat = lambda kehu_or_group: self.page.locator(f'//div[@class="searchResult"]//span[text()="{kehu_or_group}"]')
        self.input_area = self.page.locator('//div[@class="editDiv"]')  # 企微工作台-输入框
        self.send_button = self.page.locator('//div[@class="sendBox"]//button')  # 企微工作台-发送按钮
        # 企微工作台 - 聊天记录
        self.msg_l = lambda arg_for_locator: self.page.locator(f'//div[@class="mainL_T"]//div[@class="msgContent textCon"]//div[text()="{arg_for_locator}"]')
        self.chat_top_chat_name = self.page.locator('//div[@class="MsgMain_header_T_L"]/span[1]')  # 企微工作台-会话顶部-联系人名称/群聊名称
        self.create_group_button_l = self.page.locator('//div[@class="searchBox"]//span[@title="新建群聊"]')  # 企微工作台-新建群聊按钮
        # 新建群聊 - 客户名称输入框
        self.kehu_name_input_l = self.page.locator('//div[@class="ant-modal-body"]//span[@class="ant-input-wrapper ant-input-group"]//input')
        # 新建群聊 - 客户名称输入框 - 搜索按钮
        self.kehu_name_input_search_button_l = self.page.locator('//div[@class="ant-modal-content"]//div[@class="searchBox"]//button[@type="button"]')
        # 新建群聊 - 客户名称输入框 - 删除按钮
        self.kehu_name_input_delete_l = self.page.locator('//div[@class="ant-modal-body"]//span[@class="ant-input-suffix"]')
        # 新建群聊 - 客户选项
        self.kehu_option_l = lambda kehu: self.page.locator(f'//div[@class="ant-modal-body"]//div[@class="customerMain"]//span[@title="{kehu}"]')
        # 新建群聊 - 创建按钮
        self.create_button_l = self.page.locator('//div[@class="ant-modal-body"]//div[@class="InviteFriendGroupR"]//span[text()="创 建"]/..')
        # 群聊名称输入框
        self.group_name_input_l = self.page.locator('//div[@class="ant-modal-content"]//input[@id="basic_name"]')
        # 完成创建按钮
        self.finish_create_button_l = self.page.locator('//div[@class="ant-modal-content"]//span[text()="完成创建"]/..')
        # 主体
        self.zhuti_l = lambda xuhao: self.page.locator(f'//div[@class="WechatEnterpriseSubject"]//span[@class="companyWeChatName"][{xuhao}]')
        # 创建群聊界面 - -顶部的主体
        self.zhuti_in_create_group_l = self.page.locator('//div[@class="ant-modal-content"]//span[@class="ant-select-selection-search"]/..')
        # 创建群聊界面--顶部的主体--选项
        self.wecome_l = lambda wecom: self.page.locator('//span[@class="companyWeChatName"]').filter(has_text=wecom)
        self.emoji_button = self.page.locator('//div[@class="toolbarL"]//img[contains(@src, "emojiIcon")]')
        self.picture_button = self.page.locator('//div[@class="toolbarL"]//img[contains(@src, "imgIcon")]')
        self.file_button = self.page.locator('//div[@class="toolbarL"]//img[contains(@src, "fileIcon")]')
        self.msg_record_button = self.page.locator('//div[@class="toolbarL"]//img[contains(@src, "msgRecordIcon")]')
        self.send_button_in_file = self.page.locator('//div[@class="ant-modal-content"]//button[@class="ant-btn ant-btn-primary"]')

    def choose_wecome_left(self, wechat_name):
        with allure.step(f'在页面左侧点击企微：{wechat_name}'):
            self.wecome_l(wechat_name).click()

    def create_group_fuc(self, kehu_list, group_name):
        with allure.step('点击新建群聊按钮'):
            self.create_group_button_l.click()
        for kehu in kehu_list:
            with allure.step(f'在客户名称输入框中，输入客户：{kehu}'):
                self.kehu_name_input_l.fill(kehu)
            with allure.step('在客户名称输入框中，点击搜索按钮'):
                self.kehu_name_input_search_button_l.click()
            with allure.step(f'在查询结果中，勾选客户：{kehu}'):
                self.kehu_option_l(kehu).click()
            with allure.step('清空客户名称输入框'):
                self.kehu_name_input_l.clear()
        with allure.step('点击创建按钮'):
            self.create_button_l.click()
        with allure.step(f'输入群聊名称：{group_name}'):
            self.group_name_input_l.fill(group_name)
        with allure.step('点击完成创建按钮'):
            self.finish_create_button_l.click()

    def create_group(self, wechat_name, kehu_list, group_name, num=0):
        self.choose_wecome_left(wechat_name)
        if num:
            for i in range(num):
                group_name_new = group_name + '-' + str(i+1)
                self.create_group_fuc(kehu_list, group_name_new)
        else:
            self.create_group_fuc(kehu_list, group_name)

    def search_and_goin_chat(self, kehu_or_group):
        with allure.step(f'在客户名称、群名称查询输入框中输入：{kehu_or_group}'):
            self.search_input_l.fill(kehu_or_group)
        # with allure.step('点击客户名称、群名称查询输入框中的搜索按钮'):
        #     self.search_button_l.click()
        with allure.step(f'在搜索的列表中，点击：{kehu_or_group}'):
            self.search_result_chat(kehu_or_group).click()

    def send_msg_fuc(self, text='', emoji_num=0, picture_path='', file_path=''):
        if text:
            with allure.step(f'在文本输入框中，输入内容：{text}'):
                self.input_area.fill(text)
                self.send_button.click()
        if emoji_num:
            emoji = self.page.locator('//div[@class="emojiContent"]/div')
            emoji_len = emoji.count()
            with allure.step(f'发送{emoji_num}个表情'):
                count = 1
                for i in random.sample(range(0, emoji_len), emoji_num):
                    self.emoji_button.click()
                    title = emoji.nth(i).locator('img').get_attribute('title')
                    with allure.step(f'选择的第{count}个表情：{title}'):
                        emoji.nth(i).click()
                    count += 1
                self.send_button.click()
        if picture_path:
            with allure.step('上传图片'):
                with self.page.expect_file_chooser() as f:
                    self.picture_button.click()
                f.value.set_files(picture_path)
                self.send_button.click()
        if file_path:
            with allure.step('上传文件'):
                with self.page.expect_file_chooser() as f:
                    self.file_button.click()
                f.value.set_files(file_path)
                self.send_button_in_file.click()

    def send_msg(self, wechat_name, kehu_or_group, text='', emoji_num=0, picture_path='', file_path=''):
        self.choose_wecome_left(wechat_name)
        self.search_and_goin_chat(kehu_or_group)
        self.send_msg_fuc(text=text, emoji_num=emoji_num, picture_path=picture_path, file_path=file_path)




