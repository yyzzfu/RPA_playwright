import pytest

from module.jisu_page import JiSuPage


@pytest.mark.smoke
def test_jisu_create_group_task(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "极速-群聊-立即"
    wechat_name_list, user, group_name_list = data_for_test
    jisu_page = JiSuPage(pw_page)
    jisu_page.page_login(*user, base_url)
    jisu_page.navigate()
    send_content_dic = get_send_content_dic(described)
    jisu_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                send_content_dic.get('content_dic'))


def test_jisu_create_group_task_by_regular(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "极速-群聊-定时"
    wechat_name_list, user, group_name_list = data_for_test
    jisu_page = JiSuPage(pw_page)
    jisu_page.page_login(*user, base_url)
    jisu_page.navigate()
    send_content_dic = get_send_content_dic(described)
    jisu_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                send_content_dic.get('content_dic'), regular=True)


@pytest.mark.smoke
def test_jisu_create_person_task(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "极速-私聊-立即"
    wechat_name_list, user, _ = data_for_test
    jisu_page = JiSuPage(pw_page)
    jisu_page.page_login(*user, base_url)
    jisu_page.navigate()
    group_name_list = ['测试微信', '反派测试', '付益强', '中国加油']
    send_content_dic = get_send_content_dic(described)
    jisu_page.create_person_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                 send_content_dic.get('content_dic'))


def test_jisu_create_person_task_by_regular(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "极速-私聊-定时"
    wechat_name_list, user, _ = data_for_test
    jisu_page = JiSuPage(pw_page)
    jisu_page.page_login(*user, base_url)
    jisu_page.navigate()
    group_name_list = ['测试微信', '反派测试', '付益强', '中国加油']
    send_content_dic = get_send_content_dic(described)
    jisu_page.create_person_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                 send_content_dic.get('content_dic'), regular=True)
