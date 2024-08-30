class MyData:

    def data_for_test(self, kf):

        wechat_name_kf2 = ['付益强测试1']
        kehu_list_kf2 = ['测试微信', '反派测试', '付益强', '中国加油']
        group_name_list_kf2 = ['fff', ]

        wechat_name_kf3 = ['fyq测试1']
        kehu_list_kf3 = ['测试微信', '反派测试', '付益强', '中国加油']
        group_name_list_kf3 = ['yyy', 'x']

        user = {'kf3': {'other_username': ['kf5'], 'password': 'Qwer1234',
                        'create_pull_group_data': {'name_list': ['测试微信'], 'name_fixed_list': ['反派测试'],
                                                   'employee': 'kf2', 'wechat_name_list': wechat_name_kf3,
                                                   'name_pull_list': ['测试微信']},  # 批量拉群
                        'create_fast_task_data': {'wechat_name_list': ['fyq测试1']},  # 快捷任务
                        'create_gaoji_group_task_data': {'wechat_name_list': wechat_name_kf3,
                                                         'group_name_list': group_name_list_kf3},  # 高级群发--群聊群发
                        'create_gaoji_person_task_data': {'wechat_name_list': wechat_name_kf3,
                                                          'kehu_list': kehu_list_kf3},  # 高级群发--私聊群发
                        'create_gaoji_notice_task_data': {'wechat_name_list': wechat_name_kf3,
                                                          'group_name_list': group_name_list_kf3},  # 高级群发--群发公告
                        'create_group_rename_task_data': {'wechat_name_list': ['kf3'], 'group_name': '新的群名'},  # 群名任务
                        'jisu_create_group_task_data': {'wechat_name_list': wechat_name_kf3,
                                                        'group_name_list': group_name_list_kf3},  # 极速群发--群聊群发
                        'jisu_create_person_task_data': {'wechat_name_list': wechat_name_kf3,
                                                         'kehu_list': kehu_list_kf3}  # 极速群发--私聊群发
                        },
                'kf2': {'other_username': ['kf5'], 'password': 'Qwer1234',
                        'create_pull_group_data': {'name_list': ['测试微信'], 'name_fixed_list': ['反派测试'],
                                                   'employee': 'kf3', 'wechat_name_list': wechat_name_kf2,
                                                   'name_pull_list': ['测试微信']},  # 批量拉群
                        'create_fast_task_data': {'wechat_name_list': wechat_name_kf2},  # 快捷任务
                        'create_gaoji_group_task_data': {'wechat_name_list': wechat_name_kf2,
                                                         'group_name_list': group_name_list_kf2},  # 高级群发--群聊群发
                        'create_gaoji_person_task_data': {'wechat_name_list': wechat_name_kf2,
                                                          'kehu_list': kehu_list_kf2},  # 高级群发--私聊群发
                        'create_gaoji_notice_task_data': {'wechat_name_list': wechat_name_kf2,
                                                          'group_name_list': group_name_list_kf2},  # 高级群发--群发公告
                        'create_group_rename_task_data': {'wechat_name_list': ['kf2'], 'group_name': '新的群名'},  # 群名任务
                        'jisu_create_group_task_data': {'wechat_name_list': wechat_name_kf2,
                                                        'group_name_list': group_name_list_kf2},  # 极速群发--群聊群发
                        'jisu_create_person_task_data': {'wechat_name_list': wechat_name_kf2,
                                                         'kehu_list': kehu_list_kf2}  # 极速群发--私聊群发
                        }
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

    def send_content_dic(self, described):
        from utils.tools import get_path, get_my, get_time_now

        time_now = get_time_now()
        mrmy = get_my()
        task_name = f'{described}{time_now}'
        text = f'(测试){described}{time_now}：' + mrmy
        picture = get_path(r'/data_module/upload/pciture.jpg')
        video = get_path(r'/data_module/upload/video.mp4')
        link = {'title': f'链接标题{time_now}', 'address': r'http://www.baidu.com',
                'content': f'内容简介:{described}{time_now}',
                'picture_path': get_path(r'/data_module/upload/pciture.jpg')}
        file = {'file_name': f'文件名称{time_now}', 'file_path': get_path(r'/data_module/upload/file.pdf')}
        notice = f'{described}-群公告内容：{mrmy}{time_now}'
        send_content_dic = {
            "content_dic": {
                'text': text,
                'picture': picture,
                'video': video,
                'link': link,
                'file': file,
                'notice': notice,
            },
            "task_name": task_name
        }
        return send_content_dic


if __name__ == '__main__':
    print(MyData().data_for_test('all'))