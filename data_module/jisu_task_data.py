from data_module import *
from dataclasses import dataclass


@dataclass
class JiSuGroupData(As_dict):

    described = '极速-群聊-立即'
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
class JiSuPersonData(As_dict):
    described = '极速-私聊-立即'
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


if __name__ == '__main__':
    print(JiSuPersonData.as_dict_class())
