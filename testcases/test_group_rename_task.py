from testcases import *


def test_create_group_rename_task(pw_page, get_user_and_wecom_data):
    """群名任务--立即"""
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.group_rename_task_page.navigate()
    data = GroupRenameData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.group_rename_task_page.create_task_func(**data)


def test_create_group_rename_task_by_regular(pw_page, get_user_and_wecom_data):
    """群名任务--定时"""
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.group_rename_task_page.navigate()
    data = GroupRenameRegularData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.group_rename_task_page.create_task_func(**data)
