from testcases import *


@allure.epic('智能助理')
@allure.feature('极速群发')
@allure.title('群聊群发（群发对象：指定群-选择客户群）--立即发送')
# @pytest.mark.smoke
def test_jisu_create_group_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    data = JiSuGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.jisu_page.navigate()
    my_page.jisu_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('极速群发')
@allure.title('群聊群发（群发对象：指定群-选择客户群）--定时发送')
def test_jisu_create_group_task_by_regular(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    data = JiSuGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.jisu_page.navigate()
    my_page.jisu_page.create_task_func(**data, regular=5)


@allure.epic('智能助理')
@allure.feature('极速群发')
@allure.title('私聊群发（群发对象：按客户-选择客户）--立即发送')
# @pytest.mark.smoke
def test_jisu_create_person_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.jisu_page.navigate()
    data = JiSuPersonData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.jisu_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('极速群发')
@allure.title('私聊群发（群发对象：按客户-选择客户）--定时发送')
def test_jisu_create_person_task_by_regular(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.jisu_page.navigate()
    data = JiSuPersonData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.jisu_page.create_task_func(**data, regular=5)
