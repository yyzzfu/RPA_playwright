from data_module import *
from dataclasses import dataclass


@dataclass
class MuBanData(As_dict):
    muban_name = f'模板+时间戳'
    muban_disc = f'模板描述+时间戳'
    text = f'{"（测试）快捷+时间戳" + "：" + get_my()}'
