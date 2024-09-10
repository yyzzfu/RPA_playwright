class UserData:

    @staticmethod
    def data_for_test(kf):

        user = {
            'kf3': {
                'user_list': [('kf3', 'Qwer1234'), ('kf5', 'Qwer1234')],
                'wechat_name_list': ['fyq测试1'],  # 选择的企微账号
                'send_group_list': ['yyy', 'x'],  # 群发对象-指定群
                'send_customer_list': ['测试微信', '反派测试', '付益强', '中国加油'],  # 群发对象-按客户
                'agent': ['kf3'],  # 智能助理
                'pull_group': {
                    'pull_customer_list': ['测试微信'],  # '批量拉群-被邀请客户'
                    'fixed_customer_list': ['反派测试'],  # 批量拉群-新群固定客户
                    'fixed_employee': 'kf2',  # 批量拉群-新群固定员工
                },
            },
            'kf2': {
                'user_list': [('kf2', 'Qwer1234'), ('kf5', 'Qwer1234')],
                'wechat_name_list': ['付益强测试1'],
                'send_group_list': ['fff', ],
                'send_customer_list': ['测试微信', '反派测试', '付益强', '中国加油'],
                'agent': ['kf2'],
                'pull_group': {
                    'pull_customer_list': ['测试微信'],
                    'fixed_customer_list': ['反派测试'],
                    'fixed_employee': 'kf3,',
                },
            },
        }
        return user.get(kf)


if __name__ == '__main__':
    print(UserData().data_for_test('all'))
