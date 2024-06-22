from modules.group_rename_task_page import GroupNameTaskPage
from utils.tools import get_time_now


def test_create_group_rename_task(pw_page, base_url, data_for_test):
    """群名任务"""
    group_rename_page = GroupNameTaskPage(pw_page)
    group_rename_page.page_login(*data_for_test[1], base_url)

    group_rename_page.navigate()
    time_now = get_time_now()
    task_name = f'群名任务{time_now}'
    wechat_name_list = ['kf3']
    group_name = '新的群名'
    new_group_name = f'新的群名{time_now}'
    group_rename_page.create_task_func(task_name, wechat_name_list, group_name, new_group_name)


