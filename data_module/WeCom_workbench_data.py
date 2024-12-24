from data_module import *
from dataclasses import dataclass

picture_common = '图片路径'
video_common = '视频路径'
file_common = '文件路径'


@dataclass
class CreateGroupData(As_dict):

    wechat_name = '付益强测试2'  # 企微账号
    kehu_list = ['测试微信的备注-vyc', '中国加油-9kz']
    group_name = '群名+时间戳'
    num = 0  # 创建群的个数


@dataclass
class SendMsgData(As_dict):

    wechat_name = '付益强测试1'  # 企微账号
    kehu_or_group = '拉群1719032562-99'
    text = '文本内容+时间戳'
    emoji_num = 2  # 表情的个数
    picture_path = picture_common
    file_path = file_common
