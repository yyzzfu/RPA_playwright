import os
import time
import random

from playwright.sync_api import Page, Locator
import datetime


def get_path(path: str) -> str:
    if path[0] != "/":
        path = f"/{path}"
    return f"{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}{path}"


def 日期控件填写(page: Page, locator: Locator, 相对日期: int):
    temp_time = datetime.datetime.now() + datetime.timedelta(days=相对日期)
    year = temp_time.year
    month = temp_time.month
    day = temp_time.day
    locator.click()
    page.locator('.thy-calendar-year-btn').click()
    page.locator('//td[@role="gridcell"]').filter(has_text=f"{year}").locator("a").click()  # 年
    page.locator('.thy-calendar-month-btn').click()
    page.locator('//td[@role="gridcell"]').nth(month - 1).click()  # 月
    page.locator('//td[@role="gridcell"][not(contains(@class,"month"))]').filter(has_text=f"{day}").click()  # 日


def get_my():
    with open(get_path(r'/utils/mrmy.txt'), 'r', encoding='utf-8') as f:
        all = f.readlines()
        all_len = len(all)
        text = all[random.randint(0, all_len-1)]
        return text


def get_time_now(is_str=True):
    if is_str:
        return str(int(time.time()))
    else:
        return int(time.time()*1000)



if __name__ == '__main__':
    print(get_path('1.png'))
