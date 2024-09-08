from data_module import *
from dataclasses import dataclass


@dataclass
class GaoJiGroupData(As_dict):

    described = '高级-群聊-立即'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name_list = ['fyq测试1']  # 企微账号

    text = f'(测试){described}+时间戳：' + get_my()
    picture = get_path(r'/data_module/upload/pciture.jpg')
    video = get_path(r'/data_module/upload/video.mp4')
    link = {'title': f'链接标题+时间戳',
            'address': r'http://www.baidu.com+时间戳',
            'content': f'内容简介:{described}+时间戳',
            'picture_path': get_path(r'/data_module/upload/pciture.jpg')}
    file = {'file_name': f'文件名称+时间戳',
            'file_path': get_path(r'/data_module/upload/file.pdf')}


@dataclass
class GaoJiNoticeData(As_dict):

    described = '高级-群发公告-立即'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name_list = ['fyq测试1']  # 企微账号

    text = f'(测试){described}+时间戳：' + get_my()
    picture = get_path(r'/data_module/upload/pciture.jpg')
    video = get_path(r'/data_module/upload/video.mp4')
    link = {'title': f'链接标题+时间戳',
            'address': r'http://www.baidu.com+时间戳',
            'content': f'内容简介:{described}+时间戳',
            'picture_path': get_path(r'/data_module/upload/pciture.jpg')}
    file = {'file_name': f'文件名称+时间戳',
            'file_path': get_path(r'/data_module/upload/file.pdf')}
    notice = f'{described}-群公告内容：{get_my()}+时间戳'


@dataclass
class GaoJiPersonData(As_dict):
    described = '高级-私聊-立即'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name_list = ['fyq测试1']  # 企微账号
    kehu_list = ['测试微信', '反派测试', '付益强', '中国加油']

    text = f'(测试){described}+时间戳：' + get_my()
    picture = get_path(r'/data_module/upload/pciture.jpg')
    video = get_path(r'/data_module/upload/video.mp4')
    link = {'title': f'链接标题+时间戳',
            'address': r'http://www.baidu.com+时间戳',
            'content': f'内容简介:{described}+时间戳',
            'picture_path': get_path(r'/data_module/upload/pciture.jpg')}
    file = {'file_name': f'文件名称+时间戳',
            'file_path': get_path(r'/data_module/upload/file.pdf')}


if __name__ == '__main__':
    print(GaoJiPersonData.as_dict_class())
