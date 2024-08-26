from utils.tools import get_my, get_time_now
from testcases import *


@pytest.mark.smoke
def test_create_fast_task(pw_page, get_kf):
    """快捷任务"""
    my_page = PageIns.login_and_return_page_ins(pw_page, *get_kf)
    create_fast_task_data = my_page.test_data.get('create_fast_task_data')
    my_page.group_muban_page.navigate()
    time_now = get_time_now()
    muban_name = f'模板{time_now}'
    muban_disc = f'模板描述{time_now}'
    muban_text = f'{"（测试）快捷" + time_now + "：" + get_my()}'
    my_page.group_muban_page.create_muban_func(muban_name, muban_disc, muban_text)

    task_name = f'快捷任务{time_now}'
    wechat_name_list = create_fast_task_data.get('wechat_name_list')  # 选择的企微账号
    my_page.fast_task_page.navigate()
    my_page.fast_task_page.create_task_func(task_name, wechat_name_list, muban_name)


def test_create_fast_task_by_regular(pw_page, get_kf):
    """快捷任务"""
    my_page = PageIns.login_and_return_page_ins(pw_page, get_kf)
    create_fast_task_data = my_page.test_data.get('create_fast_task_data')
    my_page.group_muban_page.navigate()
    time_now = get_time_now()
    muban_name = f'模板{time_now}'
    muban_disc = f'模板描述{time_now}'
    muban_text = f'{"（测试）快捷" + time_now + "：" + get_my()}'
    my_page.group_muban_page.create_muban_func(muban_name, muban_disc, muban_text)

    task_name = f'快捷任务{time_now}'
    wechat_name_list = create_fast_task_data.get('wechat_name_list')  # 选择的企微账号
    my_page.fast_task_page.navigate()
    my_page.fast_task_page.create_task_func(task_name, wechat_name_list, muban_name, regular=True)



