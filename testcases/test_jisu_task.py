from testcases import *


# @pytest.mark.smoke
def test_jisu_create_group_task(pw_page, get_kf, kf_for_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, *get_kf)
    data = JiSuGroupData.as_dict_class(kf_for_data)
    my_page.jisu_page.navigate()
    my_page.jisu_page.create_task_func(**data)


# def test_jisu_create_group_task_by_regular(pw_page, get_kf):
#     described = "极速-群聊-定时"
#     my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
#     jisu_create_group_task_data = my_page.test_data.get('jisu_create_group_task_data')
#     wechat_name_list = jisu_create_group_task_data.get('wechat_name_list')  # 选择的企微账号
#     group_name_list = jisu_create_group_task_data.get('group_name_list')  # 群发对象--指定群聊
#     my_page.jisu_page.navigate()
#     send_content_dic = MyData().send_content_dic(described)
#     my_page.jisu_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
#                                         send_content_dic.get('content_dic'), regular=True)


# @pytest.mark.smoke
def test_jisu_create_person_task(pw_page, get_kf, kf_for_data):
    my_page = PageIns.login_and_return_page_ins(pw_page, *get_kf)
    my_page.jisu_page.navigate()
    data = JiSuPersonData.as_dict_class(kf_for_data)
    my_page.jisu_page.create_task_func(**data)


# def test_jisu_create_person_task_by_regular(pw_page, get_kf):
#     described = "极速-私聊-定时"
#     my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
#     jisu_create_person_task_data = my_page.test_data.get('jisu_create_person_task_data')
#     wechat_name_list = jisu_create_person_task_data.get('wechat_name_list')
#     kehu_list = jisu_create_person_task_data.get('kehu_list')
#     my_page.jisu_page.navigate()
#     send_content_dic = MyData().send_content_dic(described)
#     my_page.jisu_page.create_person_task(send_content_dic.get('task_name'), wechat_name_list, kehu_list,
#                                          send_content_dic.get('content_dic'), regular=True)
