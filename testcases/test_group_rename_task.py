import pytest

from module.group_rename_task_page import GroupNameTaskPage
from utils.tools import get_time_now
from testcases import *



@pytest.mark.smoke
def test_create_group_rename_task(new_context, base_url, data_for_test):
    """群名任务"""
    my_page = PageIns.new_context_and_return_page_ins(new_context)
    my_page.group_rename_task_page.navigate()
    time_now = get_time_now()
    task_name = f'群名任务{time_now}'
    wechat_name_list = ['kf3']
    group_name = '新的群名'
    new_group_name = f'新的群名{time_now}'
    my_page.group_rename_task_page.create_task_func(task_name, wechat_name_list, group_name, new_group_name)


def test_create_group_rename_task_by_regular(new_context, base_url, data_for_test):
    """群名任务"""

    my_page = PageIns.new_context_and_return_page_ins(new_context)
    my_page.group_rename_task_page.navigate()
    time_now = get_time_now()
    task_name = f'群名任务{time_now}'
    wechat_name_list = ['kf3']
    group_name = '新的群名'
    new_group_name = f'新的群名{time_now}'
    my_page.group_rename_task_page.create_task_func(task_name, wechat_name_list, group_name, new_group_name, regular=True)



