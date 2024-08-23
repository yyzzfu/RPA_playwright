from module.group_muban_page import GroupMuBanPage
from module.fast_task_page import FastTaskPage
from utils.tools import get_my, get_time_now
import pytest
from testcases import *


@pytest.mark.smoke
def test_create_fast_task(new_context, base_url, data_for_test):
    """快捷任务"""
    my_page = PageIns.new_context_and_return_page_ins(new_context)

    wechat_name_list, user, _ = data_for_test

    my_page.group_muban_page.navigate()
    time_now = get_time_now()
    muban_name = f'模板{time_now}'
    muban_disc = f'模板描述{time_now}'
    muban_text = f'{"（测试）快捷" + time_now + "：" + get_my()}'
    my_page.group_muban_page.create_muban_func(muban_name, muban_disc, muban_text)

    task_name = f'快捷任务{time_now}'
    my_page.fast_task_page.navigate()
    my_page.fast_task_page.create_task_func(task_name, wechat_name_list, muban_name)


def test_create_fast_task_by_regular(new_context, base_url, data_for_test):
    """快捷任务"""
    my_page = PageIns.new_context_and_return_page_ins(new_context)

    wechat_name_list, user, _ = data_for_test

    my_page.group_muban_page.navigate()
    time_now = get_time_now()
    muban_name = f'模板{time_now}'
    muban_disc = f'模板描述{time_now}'
    muban_text = f'{"（测试）快捷" + time_now + "：" + get_my()}'
    my_page.group_muban_page.create_muban_func(muban_name, muban_disc, muban_text)

    task_name = f'快捷任务{time_now}'
    my_page.fast_task_page.navigate()
    my_page.fast_task_page.create_task_func(task_name, wechat_name_list, muban_name, regular=True)



