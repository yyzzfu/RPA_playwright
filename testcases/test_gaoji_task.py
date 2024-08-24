from testcases import *


@pytest.mark.smoke
def test_create_gaoji_group_task(pw_page, get_kf):
    described = "高级-群聊-立即"
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_gaoji_group_task_data = my_page.test_data.get('create_gaoji_group_task_data')

    wechat_name_list = create_gaoji_group_task_data.get('wechat_name_list')  # 选择的企微账号
    group_name_list = create_gaoji_group_task_data.get('group_name_list')  # 群发对象--指定群
    my_page.gaoji_page.navigate()
    send_content_dic = MyData().send_content_dic(described)
    my_page.gaoji_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                         send_content_dic.get('content_dic'))


def test_gaoji_create_group_one_by_one_task(pw_page, get_kf):
    described = "高级-群聊-单独立即"
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_gaoji_group_task_data = my_page.test_data.get('create_gaoji_group_task_data')

    wechat_name_list = create_gaoji_group_task_data.get('wechat_name_list')  # 选择的企微账号
    group_name_list = create_gaoji_group_task_data.get('group_name_list')  # 群发对象--指定群
    my_page.gaoji_page.navigate()
    send_content_dic = MyData().send_content_dic(described)

    text = send_content_dic.get('content_dic').get('text') + '@所有人'
    send_content_dic['content_dic']['text'] = text
    my_page.gaoji_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                         send_content_dic.get('content_dic'), one_by_one=True)


def test_gaoji_create_group_by_regular(pw_page, get_kf):
    described = "高级-群聊-定时"
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_gaoji_group_task_data = my_page.test_data.get('create_gaoji_group_task_data')

    wechat_name_list = create_gaoji_group_task_data.get('wechat_name_list')  # 选择的企微账号
    group_name_list = create_gaoji_group_task_data.get('group_name_list')  # 群发对象--指定群
    my_page.gaoji_page.navigate()
    send_content_dic = MyData().send_content_dic(described)
    my_page.gaoji_page.create_group_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                         send_content_dic.get('content_dic'), regular=True)


@pytest.mark.smoke
def test_gaoji_create_person_task(pw_page, get_kf):
    described = "高级-私聊-立即"
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_gaoji_person_task_data = my_page.test_data.get('create_gaoji_person_task_data')
    my_page.gaoji_page.navigate()
    wechat_name_list = create_gaoji_person_task_data.get('wechat_name_list')  # 选择的企微账号
    kehu_list = create_gaoji_person_task_data.get('kehu_list')  # 群发对象--指定客户
    send_content_dic = MyData().send_content_dic(described)
    my_page.gaoji_page.create_person_task(send_content_dic.get('task_name'), wechat_name_list, kehu_list,
                                          send_content_dic.get('content_dic'))


def test_gaoji_create_person_task_by_regular(pw_page, get_kf):
    described = "高级-私聊-定时"
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_gaoji_person_task_data = my_page.test_data.get('create_gaoji_person_task_data')
    my_page.gaoji_page.navigate()
    wechat_name_list = create_gaoji_person_task_data.get('wechat_name_list')  # 选择的企微账号
    kehu_list = create_gaoji_person_task_data.get('kehu_list')  # 群发对象--指定客户
    send_content_dic = MyData().send_content_dic(described)
    my_page.gaoji_page.create_person_task(send_content_dic.get('task_name'), wechat_name_list, kehu_list,
                                          send_content_dic.get('content_dic'), regular=True)


@pytest.mark.smoke
def test_gaoji_create_notice_task(pw_page, get_kf):
    described = "高级-群发公告-立即"
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_gaoji_notice_task_data = my_page.test_data.get('create_gaoji_notice_task_data')
    my_page.gaoji_page.navigate()
    wechat_name_list = create_gaoji_notice_task_data.get('wechat_name_list')
    group_name_list = create_gaoji_notice_task_data.get('group_name_list')
    send_content_dic = MyData().send_content_dic(described)
    my_page.gaoji_page.create_notice_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                          send_content_dic.get('content_dic'))


def test_gaoji_create_notice_task_by_regular(pw_page, get_kf):
    described = "高级-群发公告-定时"
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_gaoji_notice_task_data = my_page.test_data.get('create_gaoji_notice_task_data')
    my_page.gaoji_page.navigate()
    wechat_name_list = create_gaoji_notice_task_data.get('wechat_name_list')
    group_name_list = create_gaoji_notice_task_data.get('group_name_list')
    send_content_dic = MyData().send_content_dic(described)
    my_page.gaoji_page.create_notice_task(send_content_dic.get('task_name'), wechat_name_list, group_name_list,
                                          send_content_dic.get('content_dic'), regular=True)
