from json import JSONDecodeError
import random

from testcases import *
from utils.tools import get_time_now


@pytest.mark.smoke
def test_create_pull_group(pw_page, global_map, request, get_kf):
    """批量拉群--创建群聊--立即"""
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_pull_group_data = my_page.test_data.get('create_pull_group_data')

    my_page.pull_group_page.navigate()
    time_now = get_time_now()
    task_name = f'拉群-创建群-立即{time_now}'  # 任务名称
    name_list = create_pull_group_data.get('name_list')  # 被邀请的客户
    name_fixed_list = create_pull_group_data.get('name_fixed_list')  # 新群固定客户
    employee = create_pull_group_data.get('employee')  # 新群固定员工
    wechat_name_list = create_pull_group_data.get('wechat_name_list')  # 选择的企微账号
    members_count = str(random.randint(10, 100))  # 目标群成员数
    group_rate = str(random.randint(60, 100))  # 预计入群率
    group_name_start_with = '拉群' + time_now + '-'  #新建群名称
    code = str(random.randint(10, 100))  # 开始编号
    my_page.pull_group_page.create_task_create_group(task_name, wechat_name_list, name_list, group_name_start_with, code,
                                             name_fixed_list, employee, members_count, group_rate)
    global_map.set('group_name_start_with', group_name_start_with)
    global_map.set(request.node.name, task_name)


def test_create_pull_group_by_regular(pw_page, global_map, request, get_kf):
    """批量拉群--在已有的群中拉人--定时"""
    try:
        group_name_start_with = global_map.get('group_name_start_with')
        if not group_name_start_with:
            raise Exception('group_name_start_with未获取到')
    except JSONDecodeError:
        raise Exception('group_name_start_with不存在')

    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_pull_group_data = my_page.test_data.get('create_pull_group_data')

    my_page.pull_group_page.navigate()
    time_now = get_time_now()
    task_name = f'拉群-群拉人-定时{time_now}'
    name_pull_list = create_pull_group_data.get('name_pull_list')  # 被邀请的客户
    wechat_name_list = create_pull_group_data.get('wechat_name_list')  # 选择的企微账号
    members_count = str(random.randint(10, 100))  # 目标群成员数
    group_rate = str(random.randint(60, 100))  # 预计入群率
    my_page.pull_group_page.create_task_pull_kehu(task_name, wechat_name_list, name_pull_list, group_name_start_with,
                                          members_count, group_rate, regular=15)
    global_map.set(request.node.name, task_name)
