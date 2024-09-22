

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
    def agent_data(cls, agent, WeCom=None):
        data = {
            'user_list': [],
            'wechat_name': [],
            'send_group_list': [],
            'send_customer_list': [],
            'agent': [],
            'pull_group': {}
        }
        if agent == 'all' and WeCom == 'all':
            for agent, agent_data in cls.test_data.items():
                for k, v in agent_data.items():
                    if isinstance(v, list):
                        data[k].extend(v)
                    elif isinstance(v, dict):
                        for l, m in v.items():
                            if isinstance(m, str):
                                data[l].append(m)
                            elif isinstance(m, list):
                                data[l].extend(m)
                            # elif isinstance(m, dict):
                            #     data[l].update(m)
            data_rel = {k: list(set(v)) for k, v in data.items()}

            # data_rel = {}
            # for k, v in data.items():
            #     if isinstance(v, list):
            #         data_rel[k] = list(set(v))
            #     elif isinstance(v, dict):
            #         data_rel[k] = v

            return data_rel
        elif agent == 'all':
            ...
        elif WeCom == 'all':
            ...
        return cls.test_data.get(agent)


if __name__ == '__main__':
    print(UserData.agent_data('all', 'all'))
