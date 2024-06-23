from modules.pull_group_page import PullGroupPage
from utils.tools import get_time_now


def test_create_pull_group_1(pw_page, base_url, data_for_test, global_map):
    """批量拉群--创建群聊"""
    pull_group_page = PullGroupPage(pw_page)
    pull_group_page.page_login(*data_for_test[1], base_url)

    pull_group_page.navigate()
    time_now = get_time_now()
    task_name = f'批量拉群-创建群{time_now}'
    wechat_name_list = ['fyq测试1']
    name_list = ['测试微信']
    name_fixed_list = ['反派测试']
    employee = 'kf2'
    members_count = '90'
    group_rate = '100'
    group_name_start_with = '拉群' + time_now + '-'
    code = '99'
    pull_group_page.create_task_create_group(task_name, wechat_name_list, name_list, group_name_start_with, code,
                                             name_fixed_list, employee, members_count, group_rate)
    global_map.set('group_name_start_with', group_name_start_with)
