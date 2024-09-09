from data_module import *
from dataclasses import dataclass


@dataclass
class FastData(As_dict):

    task_name = '快捷任务+时间戳'  # 任务名称
    wechat_name_list = '企微账号'  # 企微账号
    muban = ''  # 选择的模板

