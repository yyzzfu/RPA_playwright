import pytest

from modules.gaoji_page import GaoJiPage


@pytest.mark.smoke
def test_gaoji_create_group_task(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "高级-群聊-立即"
    wechat_name_list, user = data_for_test
    gaoji_page = GaoJiPage(pw_page)
    gaoji_page.page_login(*user, base_url)
    gaoji_page.navigate()
    group_name_list = ['yyy', 'x']
    send_content_dic = get_send_content_dic(described)
    gaoji_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                 send_content_dic.get('content_dic'))


def test_gaoji_create_group_one_by_one_task(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "高级-群聊-单独立即"
    wechat_name_list, user = data_for_test
    gaoji_page = GaoJiPage(pw_page)
    gaoji_page.page_login(*user, base_url)
    gaoji_page.navigate()
    group_name_list = ['yyy', 'x']
    send_content_dic = get_send_content_dic(described)
    text = send_content_dic.get('content_dic').get('text') + '@所有人'
    send_content_dic['content_dic']['text'] = text
    gaoji_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                 send_content_dic.get('content_dic'),
                                 one_by_one=True)


def test_gaoji_create_group_by_regular(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "高级-群聊-定时"
    wechat_name_list, user = data_for_test
    gaoji_page = GaoJiPage(pw_page)
    gaoji_page.page_login(*user, base_url)
    gaoji_page.navigate()
    group_name_list = ['yyy', 'x']
    send_content_dic = get_send_content_dic(described)
    gaoji_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                 send_content_dic.get('content_dic'),
                                 regular=True)


@pytest.mark.smoke
@pytest.mark.test_bug
def test_gaoji_create_person_task(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "高级-私聊-立即"
    wechat_name_list, user = data_for_test
    gaoji_page = GaoJiPage(pw_page)
    gaoji_page.page_login(*user, base_url)
    gaoji_page.navigate()
    wechat_name_list = wechat_name_list
    group_name_list = ['测试微信', '反派测试', '付益强', '中国加油']
    send_content_dic = get_send_content_dic(described)
    gaoji_page.create_person_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                  send_content_dic.get('content_dic'))


def test_gaoji_create_person_task_by_regular(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "高级-私聊-定时"
    wechat_name_list, user = data_for_test
    gaoji_page = GaoJiPage(pw_page)
    gaoji_page.page_login(*user, base_url)
    gaoji_page.navigate()
    wechat_name_list = wechat_name_list
    group_name_list = ['测试微信', '反派测试', '付益强', '中国加油']
    send_content_dic = get_send_content_dic(described)
    gaoji_page.create_person_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                  send_content_dic.get('content_dic'),
                                  regular=True)


@pytest.mark.smoke
def test_gaoji_create_notice_task(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "高级-群发公告-立即"
    wechat_name_list, user = data_for_test
    gaoji_page = GaoJiPage(pw_page)
    gaoji_page.page_login(*user, base_url)
    gaoji_page.navigate()
    wechat_name_list = wechat_name_list
    group_name_list = ['yyy', 'x']
    send_content_dic = get_send_content_dic(described)
    gaoji_page.create_notice_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                  send_content_dic.get('content_dic'))


def test_gaoji_create_notice_task_by_regular(pw_page, base_url, data_for_test, get_send_content_dic):
    described = "高级-群发公告-定时"
    wechat_name_list, user = data_for_test
    gaoji_page = GaoJiPage(pw_page)
    gaoji_page.page_login(*user, base_url)
    gaoji_page.navigate()
    wechat_name_list = wechat_name_list
    group_name_list = ['yyy', 'x']
    send_content_dic = get_send_content_dic(described)
    gaoji_page.create_notice_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                  send_content_dic.get('content_dic'),
                                  regular=True)
