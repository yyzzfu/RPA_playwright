from testcases import *


@allure.epic('智能助理')
@allure.feature('群名任务')
@allure.title('批量修改群名--立即发送')
def test_create_group_rename_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.group_rename_task_page.navigate()
    data = GroupRenameData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.group_rename_task_page.create_task_func(**data)


@allure.epic('智能助理')
@allure.feature('群名任务')
@allure.title('批量修改群名--定时发送')
def test_create_group_rename_task_by_regular(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.group_rename_task_page.navigate()
    data = GroupRenameRegularData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.group_rename_task_page.create_task_func(**data)
