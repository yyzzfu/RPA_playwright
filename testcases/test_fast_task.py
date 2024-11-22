from testcases import *


@allure.epic('智能助理')
@allure.feature('群发任务')
@allure.title('快捷任务--立即发送')
def test_create_fast_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.group_muban_page.navigate()
    data_1 = MuBanData.as_dict_class()
    my_page.group_muban_page.create_muban_func(**data_1)

    my_page.fast_task_page.navigate()
    data_2 = FastData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    data_2['muban'] = data_1.get('muban_name')
    my_page.fast_task_page.create_task_func(**data_2)


@allure.epic('智能助理')
@allure.feature('群发任务')
@allure.title('快捷任务--定时发送')
def test_create_fast_task_by_regular(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.group_muban_page.navigate()
    data_1 = MuBanData.as_dict_class()
    my_page.group_muban_page.create_muban_func(**data_1)

    my_page.fast_task_page.navigate()
    data_2 = FastData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    data_2['muban'] = data_1.get('muban_name')
    my_page.fast_task_page.create_task_func(**data_2, regular=5)



