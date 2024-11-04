from testcases import *


@allure.epic('智能助理')
@allure.feature('高级群发')
@allure.title('群聊群发（群发对象：指定群-选择客户群）--立即发送')
def test_create_gaoji_group_task(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.gaoji_page.navigate()
    data = GaoJiGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('高级群发')
@allure.title('群聊群发（群发对象：指定群-选择客户群）--定时发送')
def test_create_gaoji_group_task_by_regular(new_context, get_user_and_wecom_data):
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.gaoji_page.navigate()
    data = GaoJiGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.create_task_func(**data, regular=5)


@allure.epic('智能助理')
@allure.feature('高级群发')
@allure.title('群聊群发（群发对象：按条件-所有客户群）--立即发送')
def test_create_gaoji_group_all_group_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.gaoji_page.navigate()
    data = GaoJiGroupDataAllGroup.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.create_task_func(**data, regular=5)


@allure.epic('智能助理')
@allure.feature('高级群发')
@allure.title('群聊群发（群发对象：指定群-选择客户群-指定的群单独发送）--立即发送')
def test_gaoji_create_group_one_by_one_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.gaoji_page.navigate()
    data = GaoJiGroupDataOneByOne.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('高级群发')
@allure.title('私聊群发（群发对象：按客户-指定客户）--立即发送')
# @pytest.mark.smoke
def test_gaoji_create_person_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    data = GaoJiPersonData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.navigate()
    my_page.gaoji_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('高级群发')
@allure.title('群发公告（群发对象：指定群-选择客户群）--立即发送')
# @pytest.mark.smoke
def test_gaoji_create_notice_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    data = GaoJiNoticeData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.navigate()
    my_page.gaoji_page.create_task_func(**data)
