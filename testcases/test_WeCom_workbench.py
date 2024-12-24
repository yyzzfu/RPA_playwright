from module import WeComWorkbenchPage
from testcases import *


@allure.epic('智能助理')
@allure.feature('企微工作台')
@allure.title('创建群聊')
def test_create_group(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.home_page.login_info.click()
    with my_page.page.expect_popup() as new:
        my_page.home_page.WeCom_workbench.click()
    WeCom_workbench_page = WeComWorkbenchPage(new.value)
    data = CreateGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    WeCom_workbench_page.create_group(**data)


@allure.epic('智能助理')
@allure.feature('企微工作台')
@allure.title('发送消息')
def test_send_msg(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.home_page.login_info.click()
    with my_page.page.expect_popup() as new:
        my_page.home_page.WeCom_workbench.click()
    WeCom_workbench_page = WeComWorkbenchPage(new.value)
    data = SendMsgData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    WeCom_workbench_page.send_msg(**data)


