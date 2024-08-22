from modules.group_muban_page import GroupMuBanPage
from modules.fast_task_page import FastTaskPage
from utils.tools import get_my, get_time_now
import pytest


@pytest.mark.smoke
def test_create_fast_task(pw_page, base_url, data_for_test):
    """快捷任务"""
    muban_page = GroupMuBanPage(pw_page)
    wechat_name_list, user, _ = data_for_test
    muban_page.page_login(*user, base_url)

    muban_page.navigate()
    time_now = get_time_now()
    muban_name = f'模板{time_now}'
    muban_disc = f'模板描述{time_now}'
    muban_text = f'{"（测试）快捷任务" + time_now + "：" + get_my()}'
    muban_page.create_muban_func(muban_name, muban_disc, muban_text)

    fast_page = FastTaskPage(pw_page)
    task_name = f'快捷任务{time_now}'
    fast_page.navigate()
    fast_page.create_task_func(task_name, wechat_name_list, muban_name)


def test_create_fast_task_by_regular(pw_page, base_url, data_for_test):
    """快捷任务"""
    muban_page = GroupMuBanPage(pw_page)
    wechat_name_list, user, _ = data_for_test
    muban_page.page_login(*user, base_url)

    muban_page.navigate()
    time_now = get_time_now()
    muban_name = f'模板{time_now}'
    muban_disc = f'模板描述{time_now}'
    muban_text = f'{"（测试）快捷任务" + time_now + "：" + get_my()}'
    muban_page.create_muban_func(muban_name, muban_disc, muban_text)

    fast_page = FastTaskPage(pw_page)
    task_name = f'快捷任务{time_now}'
    fast_page.navigate()
    fast_page.create_task_func(task_name, wechat_name_list, muban_name, regular=True)



