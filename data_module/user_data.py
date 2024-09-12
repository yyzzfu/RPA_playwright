class UserData:
    test_data = {
        'agent1': {
            'user_list': [('kf3', 'Qwer1234'), ('kf5', 'Qwer1234')],
            'WeCom1': {
                'wechat_name': 'fyq测试1',  # 选择的企微账号
                'send_group_list': ['yyy', 'x'],  # 群发对象-指定群
                'send_customer_list': ['测试微信', '反派测试', '付益强', '中国加油'],  # 群发对象-按客户
                'agent': 'kf3',  # 群名任务-智能助理
                'pull_customer_list': ['测试微信'],  # 批量拉群-被邀请客户
                'fixed_customer_list': ['反派测试'],  # 批量拉群-新群固定客户
                'fixed_employee': 'kf2',  # 批量拉群-新群固定员工
                },
            'WeCom2': {
                'wechat_name': 'fyq测试2',
                'send_group_list': ['qqq'],
                'send_customer_list': ['测试微信', '中国加油'],
                'agent': 'kf3',
                'pull_customer_list': ['测试微信'],
                'fixed_customer_list': ['中国加油'],
                'fixed_employee': 'kf2',
                },
        },
        'agent2': {
            'user_list': [('kf2', 'Qwer1234'), ('kf5', 'Qwer1234')],
            'WeCom1': {
                'wechat_name': '付益强测试1',
                'send_group_list': ['fff'],
                'send_customer_list': ['测试微信', '反派测试', '付益强', '中国加油'],
                'agent': 'kf2',
                'pull_customer_list': ['测试微信'],
                'fixed_customer_list': ['反派测试'],
                'fixed_employee': 'kf3',
                },
            'WeCom2': {
                'wechat_name': '付益强测试2',
                'send_group_list': ['zzz'],
                'send_customer_list': ['测试微信', '反派测试'],
                'agent': 'kf2',
                'pull_customer_list': ['测试微信'],
                'fixed_customer_list': ['反派测试'],
                'fixed_employee': 'kf3',
            }
        },
    }

    @classmethod
    def agent_data(cls, agent, WeCom=None):

        if agent == 'all' and WeCom == 'all':
           ...
        elif agent == 'all':
            ...
        elif WeCom == 'all':
            ...
        return cls.test_data.get(agent)


if __name__ == '__main__':
    # print(UserData.agent_data('all', 'all'))

    # 定义两个字典
    WeCom1 = {
        'wechat_name': 'fyq测试1',
        'send_group_list': ['yyy', 'x'],
        'send_customer_list': ['测试微信', '反派测试', '付益强', '中国加油'],
        'agent': 'kf3',
        'pull_customer_list': ['测试微信'],
        'fixed_customer_list': ['反派测试'],
        'fixed_employee': 'kf2',
    }

    WeCom2 = {
        'wechat_name': 'fyq测试2',
        'send_group_list': ['qqq'],
        'send_customer_list': ['测试微信', '中国加油'],
        'agent': 'kf3',
        'pull_customer_list': ['测试微信'],
        'fixed_customer_list': ['中国加油'],
        'fixed_employee': 'kf2',
    }

    # 创建一个新的字典来存储合并后的结果
    merged_dict = {}

    # 遍历第一个字典的每一个 key-value 对
    for key, value in WeCom1.items():
        # 如果这个 key 也存在于第二个字典中
        if key in WeCom2:
            # 将两个 value 合并成一个列表
            merged_dict[key] = value + WeCom2[key] if isinstance(value, list) else [value, WeCom2[key]]
        else:
            # 如果这个 key 只存在于第一个字典中，直接添加到结果字典中
            merged_dict[key] = value

    # 遍历第二个字典，添加那些只存在于第二个字典中的 key-value 对
    for key, value in WeCom2.items():
        if key not in merged_dict:
            merged_dict[key] = value

    # 打印合并后的字典
    print(merged_dict)


