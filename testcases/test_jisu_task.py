from modules.jisu_page import JiSuPage
from utils.tools import get_path, get_my, get_time_now


def test_jisu_create_group_task(pw_page, base_url, data_for_test):
    """极速群发-群聊群发"""
    wechat_name_list, user = data_for_test
    jisu_page = JiSuPage(pw_page)
    jisu_page.page_login(*user, base_url)
    jisu_page.navigate()
    time_now = get_time_now()
    task_name = f'极速-群聊群发{time_now}'
    wechat_name_list = wechat_name_list

    group_name_list = ['yyy', 'x']
    send_content_dic = {'text': f'({time_now}测试--极速群发-群聊群发)' + get_my(),
                        'picture': get_path(r'/upload/pciture.jpg'),
                        'video': get_path(r'/upload/video.mp4'),
                        'link': {'title': f'这是链接的标题{time_now}', 'address': r'http://www.baidu.com',
                                 'content': f'这是内容简介{time_now}', 'picture_path': get_path(r'/upload/pciture.jpg')},
                        'file': {'file_name': f'这是文件的名称{time_now}', 'file_path': get_path(r'/upload/file.pdf')}}

    jisu_page.create_group_task(task_name, wechat_name_list, group_name_list, send_content_dic)


def test_jisu_create_person_task(pw_page, base_url, data_for_test):
    wechat_name_list, user = data_for_test
    jisu_page = JiSuPage(pw_page)
    jisu_page.page_login(*user, base_url)
    jisu_page.navigate()
    time_now = get_time_now()
    task_name = f'极速-私聊群发{time_now}'
    wechat_name_list = wechat_name_list
    group_name_list = ['测试微信', '反派测试', '付益强', '中国加油']
    send_content_dic = {'text': f'({time_now}测试--极速群发-私聊群发)' + get_my(),
                        'picture': get_path(r'/upload/pciture.jpg'),
                        'video': get_path(r'/upload/video.mp4'),
                        'link': {'title': f'这是链接的标题{time_now}', 'address': r'http://www.baidu.com',
                                 'content': f'这是内容简介{time_now}', 'picture_path': get_path(r'/upload/pciture.jpg')},
                        'file': {'file_name': f'这是文件的名称{time_now}', 'file_path': get_path(r'/upload/file.pdf')}}

    jisu_page.create_person_task(task_name, wechat_name_list, group_name_list, send_content_dic)
