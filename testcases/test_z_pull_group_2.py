from modules.pull_group_page import PullGroupPage
from utils.tools import get_time_now


def test_create_pull_group_2(pw_page, base_url, data_for_test, global_map):
    """批量拉群--在已有的群中拉人"""
    pull_group_page = PullGroupPage(pw_page)
    pull_group_page.page_login(*data_for_test[1], base_url)

    pull_group_page.navigate()
    time_now = get_time_now()
    task_name = f'批量拉群-群拉人{time_now}'
    wechat_name_list = ['fyq测试1']
    name_list = ['测试微信']
    members_count = '90'
    group_rate = '100'
    group_name_start_with = global_map.get('group_name_start_with')

    pull_group_page.create_task_pull_kehu(task_name, wechat_name_list, name_list, group_name_start_with,
                                          members_count, group_rate)
