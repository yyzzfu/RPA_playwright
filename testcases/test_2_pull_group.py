from json import JSONDecodeError
import random
from testcases import *

import pytest

from module.pull_group_page import PullGroupPage
from utils.tools import get_time_now


@pytest.mark.smoke
def test_create_pull_group(pw_page, base_url, data_for_test, global_map, request):
    """批量拉群--创建群聊--立即"""
    my_page = PageIns.login_and_return_page_ins(pw_page)

    wechat_name_list, user, _ = data_for_test
    my_page.pull_group_page.navigate()
    time_now = get_time_now()
    task_name = f'拉群-创建群-立即{time_now}'
    name_list = ['测试微信']
    name_fixed_list = ['反派测试']
    employee = 'kf2'
    members_count = str(random.randint(10, 100))
    group_rate = str(random.randint(60, 100))
    group_name_start_with = '拉群' + time_now + '-'
    code = str(random.randint(10, 100))
    my_page.pull_group_page.create_task_create_group(task_name, wechat_name_list, name_list, group_name_start_with, code,
                                             name_fixed_list, employee, members_count, group_rate)
    global_map.set('group_name_start_with', group_name_start_with)
    global_map.set(request.node.name, task_name)


def test_create_pull_group_by_regular(new_context, base_url, data_for_test, global_map, request):
    """批量拉群--在已有的群中拉人--定时"""
    try:
        group_name_start_with = global_map.get('group_name_start_with')
        if not group_name_start_with:
            raise Exception('group_name_start_with未获取到')
    except JSONDecodeError:
        raise Exception('group_name_start_with不存在')

    my_page = PageIns.new_context_and_return_page_ins(new_context)

    wechat_name_list, user, _ = data_for_test
    my_page.pull_group_page.navigate()
    time_now = get_time_now()
    task_name = f'拉群-群拉人-定时{time_now}'
    name_list = ['测试微信']
    members_count = str(random.randint(10, 100))
    group_rate = str(random.randint(60, 100))
    my_page.pull_group_page.create_task_pull_kehu(task_name, wechat_name_list, name_list, group_name_start_with,
                                          members_count, group_rate, regular=15)
    global_map.set(request.node.name, task_name)

