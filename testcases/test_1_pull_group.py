from testcases import *


def test_create_pull_group(pw_page, global_map, get_user_and_wecom_data):
    """批量拉群--创建群聊--立即"""
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    data = PullGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.pull_group_page.navigate()
    my_page.pull_group_page.create_task_create_group(**data)


@pytest.mark.smoke
def test_create_pull_group1(new_context, global_map, get_user_and_wecom_data):
    """批量拉群--创建群聊--立即"""

    data = PullGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    # if not data.get('pull_group'):
    #     get_user_and_wecom_data = UserData.test_data.popitem()
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.pull_group_page.navigate()
    my_page.pull_group_page.create_task_create_group(**data)
    assert 0


# def test_create_pull_group_by_regular(pw_page, global_map, request, get_kf):
#     """批量拉群--在已有的群中拉人--定时"""
#     try:
#         group_name_start_with = global_map.get('group_name_start_with')
#         if not group_name_start_with:
#             raise Exception('group_name_start_with未获取到')
#     except JSONDecodeError:
#         raise Exception('group_name_start_with不存在')
#
#     my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
#     create_pull_group_data = my_page.test_data.get('create_pull_group_data')
#
#     my_page.pull_group_page.navigate()
#     time_now = get_time_now()
#     task_name = f'拉群-群拉人-定时{time_now}'
#     name_pull_list = create_pull_group_data.get('name_pull_list')  # 被邀请的客户
#     wechat_name_list = create_pull_group_data.get('wechat_name_list')  # 选择的企微账号
#     members_count = str(random.randint(10, 100))  # 目标群成员数
#     group_rate = str(random.randint(60, 100))  # 预计入群率
#     my_page.pull_group_page.create_task_pull_kehu(task_name, wechat_name_list, name_pull_list, group_name_start_with,
#                                           members_count, group_rate, regular=15)
#     global_map.set(request.node.name, task_name)
