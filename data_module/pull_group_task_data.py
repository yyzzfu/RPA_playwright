from data_module import *
from dataclasses import dataclass


@dataclass
class PullGroupData(As_dict):

    task_name = '拉群-创建群-立即+时间戳'  # 任务名称
    wechat_name_list = ['fyq测试1']  # 企微账号
    name_list = ['测试微信']  # 被邀请客户
    自动新建群聊 = '开启'  # 自动新建群聊
    new_group_name = '拉群+时间戳'  # 新群名称
    code = '随机数(10-100)'  # 编号
    name_fixed_list = ['反派测试']  # 新群固定客户
    employee = 'kf2'  # 新群固定员工
    members_count = '随机数(10-100)'  # 目标群成员数
    group_rate = '随机数(60-100)'  # 预计入群率
    # 发送类型 = '单次定时'  # 发送类型
    # 时间设置 = '50'  # 分钟  # 时间设置
