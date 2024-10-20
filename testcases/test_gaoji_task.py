from testcases import *


def test_create_gaoji_group_task(new_context, get_user_and_wecom_data):
    """群发对象-指定群-选择客户群"""
    my_page = PageIns.new_context_and_return_page_ins(new_context, get_user_and_wecom_data.get('user'))
    my_page.gaoji_page.navigate()
    data = GaoJiGroupData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.create_task_func(**data)


def test_create_gaoji_group_all_group_task(pw_page, get_user_and_wecom_data):
    """群发对象-按条件-所有客户群"""
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.gaoji_page.navigate()
    data = GaoJiGroupDataAllGroup.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.create_task_func(**data)


def test_gaoji_create_group_one_by_one_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    my_page.gaoji_page.navigate()
    data = GaoJiGroupDataOneByOne.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.create_task_func(**data)


# def test_gaoji_create_group_by_regular(pw_page, get_kf):
#     described = "高级-群聊-定时"
#     my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)get_user_and_marker
#     create_gaoji_group_task_data = my_page.test_data.get('create_gaoji_group_task_data')
#
#     wechat_name_list = create_gaoji_group_task_data.get('wechat_name_list')  # 选择的企微账号
#     group_name_list = create_gaoji_group_task_data.get('group_name_list')  # 群发对象--指定群
#     my_page.gaoji_page.navigate()
#     send_content_dic = MyData().send_content_dic(described)
#     my_page.gaoji_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
#                                          send_content_dic.get('content_dic'), regular=True)


# @pytest.mark.smoke
def test_gaoji_create_person_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    data = GaoJiPersonData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.navigate()
    my_page.gaoji_page.create_task_func(**data)


# def test_gaoji_create_person_task_by_regular(pw_page, get_kf):
#     described = "高级-私聊-定时"
#     my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
#     create_gaoji_person_task_data = my_page.test_data.get('create_gaoji_person_task_data')
#     my_page.gaoji_page.navigate()
#     wechat_name_list = create_gaoji_person_task_data.get('wechat_name_list')  # 选择的企微账号
#     kehu_list = create_gaoji_person_task_data.get('kehu_list')  # 群发对象--指定客户
#     send_content_dic = MyData().send_content_dic(described)
#     my_page.gaoji_page.create_person_task(send_content_dic.get('task_name'), wechat_name_list, kehu_list,
#                                           send_content_dic.get('content_dic'), regular=True)


# @pytest.mark.smoke
def test_gaoji_create_notice_task(pw_page, get_user_and_wecom_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, get_user_and_wecom_data.get('user'))
    data = GaoJiNoticeData.as_dict_class(get_user_and_wecom_data.get('WeCom_data'))
    my_page.gaoji_page.navigate()
    my_page.gaoji_page.create_task_func(**data)


# def test_gaoji_create_notice_task_by_regular(pw_page, get_kf):
#     described = "高级-群发公告-定时"
#     my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
#     create_gaoji_notice_task_data = my_page.test_data.get('create_gaoji_notice_task_data')
#     my_page.gaoji_page.navigate()
#     wechat_name_list = create_gaoji_notice_task_data.get('wechat_name_list')
#     group_name_list = create_gaoji_notice_task_data.get('group_name_list')
#     send_content_dic = MyData().send_content_dic(described)
#     my_page.gaoji_page.create_notice_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
#                                           send_content_dic.get('content_dic'), regular=True)
