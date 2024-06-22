from modules.group_muban_page import GroupMuBanPage
from modules.fast_task_page import FastTaskPage
from utils.tools import get_my, get_time_now
import pytest


@pytest.mark.skip()
def test_create_fast_task(pw_page, base_url, data_for_test):
    muban_page = GroupMuBanPage(pw_page)
    muban_page.page_login(*data_for_test[1], base_url)

    muban_page.navigate()
    time_now = get_time_now()
    muban_name = f'模板{time_now}'
    muban_disc = f'模板描述{time_now}'
    muban_text = f'{get_my() + time_now + "（测试）--快捷任务"}'
    muban_page.create_muban_func(muban_name, muban_disc, muban_text)

    fast_page = FastTaskPage(pw_page)
    task_name = f'快捷任务{time_now}'
    wechat_name_list = ['fyq测试1']
    fast_page.navigate()
    fast_page.create_task_func(task_name, wechat_name_list, muban_name)
1



