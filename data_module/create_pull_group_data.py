from data_module import *
from dataclasses import dataclass


@dataclass
class CreatePullGroupData(As_dict):
    name_list = '测试微信'
    name_fixed_list = '反派测试'
    employee = 'kf2'
    wechat_name_list = ['fyq测试1']
