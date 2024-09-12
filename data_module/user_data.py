class UserData:
    test_data = {
        'agent1': {
            'user_list': [('kf3', 'Qwer1234'), ('kf5', 'Qwer1234')],
            'WeCom1': {
                'wechat_name': 'fyq测试1',  # 选择的企微账号
                'send_group_list': ['yyy', 'x'],  # 群发对象-指定群
                'send_customer_list': ['测试微信', '反派测试', '付益强', '中国加油'],  # 群发对象-按客户
                'agent': 'kf3',  # 群名任务-智能助理
                'pull_group': {
                    'pull_customer_list': ['测试微信'],  # 批量拉群-被邀请客户
                    'fixed_customer_list': ['反派测试'],  # 批量拉群-新群固定客户
                    'fixed_employee': 'kf2',  # 批量拉群-新群固定员工
                },
            },
            'WeCom2': {
                'wechat_name': 'fyq测试2',
                'send_group_list': ['qqq'],
                'send_customer_list': ['测试微信', '中国加油'],
                'agent': 'kf3',
                'pull_group': {
                    'pull_customer_list': ['测试微信'],
                    'fixed_customer_list': ['中国加油'],
                    'fixed_employee': 'kf2',
                },
            }
        },
        'agent2': {
            'user_list': [('kf2', 'Qwer1234'), ('kf5', 'Qwer1234')],
            'WeCom1': {
                'wechat_name': '付益强测试1',
                'send_group_list': ['fff'],
                'send_customer_list': ['测试微信', '反派测试', '付益强', '中国加油'],
                'agent': 'kf2',
                'pull_group': {
                    'pull_customer_list': ['测试微信'],
                    'fixed_customer_list': ['反派测试'],
                    'fixed_employee': 'kf3',
                },
            },
            'WeCom2': {
                'wechat_name': '付益强测试2',
                'send_group_list': ['zzz'],
                'send_customer_list': ['测试微信', '反派测试'],
                'agent': 'kf2',
                'pull_group': {
                    'pull_customer_list': ['测试微信'],
                    'fixed_customer_list': ['反派测试'],
                    'fixed_employee': 'kf3',
                },
            }
        },
    }

    @classmethod
    def data_template(cls):
        data_template = {
            'user_list': list,
            'wechat_name': list,
            'send_group_list': list,
            'send_customer_list': list,
            'agent': list,
            'pull_group': {
                'pull_customer_list': list,
                'fixed_customer_list': list,
                'fixed_employee': list,
            }
        }
        return data_template

    @classmethod
    def agent_data(cls, agent, WeCom=None):
        data_template = cls.data_template()
        if agent == 'all' and WeCom == 'all':
            for agent, agent_data in cls.test_data.items():
                for k, v in agent_data:
                    data_template[k].append(v)
        elif agent == 'all':
            ...
        elif WeCom == 'all':
            ...
        return cls.test_data.get(agent)


if __name__ == '__main__':
    print(UserData.data_template())
