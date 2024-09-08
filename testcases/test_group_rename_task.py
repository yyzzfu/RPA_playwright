from utils.tools import get_time_now
from testcases import *


def test_create_group_rename_task(pw_page, get_kf):
    """群名任务"""
    my_page = PageIns.login_and_return_page_ins(pw_page, *get_kf)
    my_page.group_rename_task_page.navigate()
    data = GroupRenameData.as_dict_class()
    my_page.group_rename_task_page.create_task_func(**data)



# def test_create_group_rename_task_by_regular(pw_page, get_kf):
#     """群名任务"""
#     my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
#     create_group_rename_task_data = my_page.test_data.get('create_group_rename_task_data')
#     my_page.group_rename_task_page.navigate()
#     time_now = get_time_now()
#     task_name = f'群名任务{time_now}'
#     wechat_name_list = create_group_rename_task_data.get('wechat_name_list')  # 选择螳螂智能助理
#     group_name = create_group_rename_task_data.get('group_name')  # 选择群组--指定群组
#     new_group_name = f'新的群名{time_now}'  # 新群名
#     my_page.group_rename_task_page.create_task_func(task_name, wechat_name_list, group_name, new_group_name, regular=True)