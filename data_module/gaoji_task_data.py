from data_module import *
from dataclasses import dataclass


@dataclass
class GaoJiGroupData(As_dict):

    described = '高级-群聊-立即'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name = '企微账号'  # 企微账号
    send_name_list = '群发对象-指定群'
    text = f'(测试){described}+时间戳：+名人名言'
    picture = '图片路径'
    video = '视频路径'
    link = {
        'title': '链接标题+时间戳',
        'address': r'http://www.baidu.com+时间戳',
        'content': f'内容简介:{described}+时间戳',
        'picture_path': '图片路径'
    }
    file = {
        'file_name': f'文件名称+时间戳',
        'file_path': '文件路径'
    }
    task_type = '群聊群发'


@dataclass
class GaoJiGroupDataOneByOne(As_dict):

    described = '高级-群聊-立即'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name = '企微账号'  # 企微账号
    send_name_list = '群发对象-指定群'
    text = f'(测试){described}+时间戳：+名人名言+@所有人'
    picture = '图片路径'
    video = '视频路径'
    link = {
        'title': '链接标题+时间戳',
        'address': r'http://www.baidu.com/+时间戳',
        'content': f'内容简介:{described}+时间戳',
        'picture_path': '图片路径'
    }
    file = {
        'file_name': '文件名称+时间戳',
        'file_path': '文件路径'
    }
    task_type = '群聊群发'
    one_by_one = True


@dataclass
class GaoJiNoticeData(As_dict):

    described = '高级-群发公告-立即'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name = '企微账号'  # 企微账号
    send_name_list = '群发对象-指定群'
    text = f'(测试){described}+时间戳：+名人名言'
    picture = '图片路径'
    video = '视频路径'
    link = {
        'title': '链接标题+时间戳',
        'address': r'http://www.baidu.com/+时间戳',
        'content': f'内容简介:{described}+时间戳',
        'picture_path': '图片路径'
    }
    file = {
        'file_name': '文件名称+时间戳',
        'file_path': '文件路径'
    }
    notice = f'{described}-群公告内容：+名人名言+时间戳'
    task_type = '群发公告'


@dataclass
class GaoJiPersonData(As_dict):
    described = '高级-私聊-立即'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name = '企微账号'  # 企微账号
    send_name_list = '群发对象-按客户'
    text = f'(测试){described}+时间戳：+名人名言'
    picture = '图片路径'
    video = '视频路径'
    link = {
        'title': f'链接标题+时间戳',
        'address': r'http://www.baidu.com/+时间戳',
        'content': f'内容简介:{described}+时间戳',
        'picture_path': '图片路径'
    }
    file = {
        'file_name': '文件名称+时间戳',
        'file_path': '文件路径'
    }
    task_type = '私聊群发'


if __name__ == '__main__':
    print(GaoJiPersonData.as_dict_class())
