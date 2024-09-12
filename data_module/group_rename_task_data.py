from data_module import *
from dataclasses import dataclass


@dataclass
class GroupRenameData(As_dict):

    task_name = '群名任务-立即+时间戳'  # 任务名称
    agent = '智能助理'  # 选择螳螂智能助理
    group_name = '新的群名'  # 选择群组--指定群组
    new_group_name = f'新的群名+时间戳'  # 新群名


@dataclass
class GroupRenameRegularData(As_dict):

    task_name = '群名任务-立即+时间戳'  # 任务名称
    agent = '智能助理'  # 选择螳螂智能助理
    group_name = '新的群名'  # 选择群组--指定群组
    new_group_name = f'新的群名+时间戳'  # 新群名
    regular = True      # 定时任务


