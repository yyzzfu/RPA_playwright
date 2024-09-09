class UserData:

    def data_for_test(self, kf):

        user = {
            'kf3': {'other_username':
                        ['kf5'],
                    'password': 'Qwer1234',
                    'wechat_name_list':  # 选择的企微账号
                        ['fyq测试1'],
                    'send_group_list':  # 群发对象-指定群
                        ['yyy', 'x'],
                    'send_customer_list':  # 群发对象-按客户
                        ['测试微信', '反派测试', '付益强', '中国加油'],
                    'agent':  # 智能助理
                        ['kf3']
                    },
            'kf2': {'other_username':
                        ['kf5'],
                    'password': 'Qwer1234',
                    'wechat_name_list':
                        ['付益强测试1'],
                    'send_group_list':
                        ['fff', ],
                    'send_customer_list':
                        ['测试微信', '反派测试', '付益强', '中国加油'],
                    'agent':
                        ['kf2']
                    },
        }
        if kf == 'all':
            all_account = {}
            for k, v in user.items():
                account = []
                account.append(k)
                for i in v.get('other_username'):
                    account.append(i)
                all_account[k] = account
            return all_account
        return user.get(kf)


if __name__ == '__main__':
    print(UserData().data_for_test('all'))
