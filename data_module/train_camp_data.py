from data_module import *
from dataclasses import dataclass

picture_common = '图片路径'
video_common = '视频路径'
link_common = {
    'title': '+时间戳',
    'address': r'http://www.baidu.com+时间戳',
    'content': f'内容简介: +时间戳',
    'picture_path': '图片路径'
}
file_common = {
    'file_name': f'文件名称+时间戳',
    'file_path': '文件路径'
}
train_camp = 'fyq测试'
camp = '1114-1'


@dataclass
class TrainCampGaoJiGroupData(As_dict):

    task_type_1 = '高级群发'
    task_type_2 = '群聊群发'
    text = f'(测试){task_type_1}+ {task_type_2}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    mini_program = True
    train_camp = train_camp
    camp = camp


@dataclass
class TrainCampGaoJiGroupDataOneByOne(As_dict):
    task_type_1 = '高级群发'
    task_type_2 = '群聊群发'
    text = f'(测试){task_type_1}+ {task_type_2}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    mini_program = True
    train_camp = train_camp
    camp = camp
    one_by_one = True


@dataclass
class TrainCampGaoJiNoticeData(As_dict):
    task_type_1 = '高级群发'
    task_type_2 = '群公告'
    text = f'(测试){task_type_1}+ {task_type_2}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    mini_program = True
    train_camp = train_camp
    camp = camp
    notice = f'群公告内容：' + text


@dataclass
class TrainCampGaoJiPersonData(As_dict):
    task_type_1 = '高级群发'
    task_type_2 = '私聊群发'
    text = f'(测试){task_type_1}+ {task_type_2}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    mini_program = True
    train_camp = train_camp
    camp = camp
    send_object_type = '按条件'


@dataclass
class TrainCampJiSuGroupData(As_dict):

    task_type_1 = '极速群发'
    task_type_2 = '群聊群发'
    text = f'(测试){task_type_1}+ {task_type_2}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    mini_program = True
    train_camp = train_camp
    camp = camp


@dataclass
class TrainCampJiSuPersonData(As_dict):
    task_type_1 = '极速群发'
    task_type_2 = '私聊群发'
    text = f'(测试){task_type_1}+ {task_type_2}+时间戳：+名人名言'
    picture = picture_common
    video = video_common
    link = link_common
    file = file_common
    mini_program = True
    train_camp = train_camp
    camp = camp
    send_object_type = '按条件'
