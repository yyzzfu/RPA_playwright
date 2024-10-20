from data_module import *
from dataclasses import dataclass

picture_common = '图片路径'
video_common = '视频路径'
link_common = {
    'title': '链接标题+时间戳',
    'address': r'http://www.baidu.com+时间戳',
    'content': f'内容简介: +时间戳',
    'picture_path': '图片路径'
}
file_common = {
    'file_name': f'文件名称+时间戳',
    'file_path': '文件路径'
}


@dataclass
class GaoJiGroupData(As_dict):

    described = '高级-群聊-立即'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name = '企微账号'  # 企微账号
    send_object_type = '指定群'
    send_name_list = '群发对象-指定群'
    text = f'(测试){described}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    task_type = '群聊群发'


@dataclass
class GaoJiGroupDataAllGroup(As_dict):

    described = '高级-群聊-所有群'
    task_name = f'{described}+时间戳'  # 任务名称
    wechat_name = '企微账号'  # 企微账号
    send_object_type = '按条件'
    send_name_list = '群发对象-指定群'
    text = f'(测试){described}+时间戳：+名人名言'
    picture = ''
    video = ''
    link = ''
    file = ''
    task_type = '群聊群发'


@dataclass
class GaoJiGroupDataOneByOne(As_dict):

    described = '高级-群聊-立即'
    task_name = f'{described}+时间戳'
    wechat_name = '企微账号'
    send_object_type = '指定群'
    send_name_list = '群发对象-指定群'
    text = f'(测试){described}+时间戳：+名人名言+@所有人'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    task_type = '群聊群发'
    one_by_one = True


@dataclass
class GaoJiNoticeData(As_dict):

    described = '高级-群发公告-立即'
    task_name = f'{described}+时间戳'
    wechat_name = '企微账号'
    send_object_type = '指定群'
    send_name_list = '群发对象-指定群'
    text = f'(测试){described}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    notice = f'{described}-群公告内容：+名人名言+时间戳'
    task_type = '群发公告'


@dataclass
class GaoJiPersonData(As_dict):
    described = '高级-私聊-立即'
    task_name = f'{described}+时间戳'
    wechat_name = '企微账号'
    send_object_type = '按客户'
    send_name_list = '群发对象-按客户'
    text = f'(测试){described}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    task_type = '私聊群发'


if __name__ == '__main__':
    print(GaoJiPersonData.as_dict_class())
