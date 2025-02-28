import os
import re
import time
import random
import datetime

import requests


def get_path(path: str = None):
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if path:
        if "/" in path:
            path = path.split("/")
        elif "\\" in path:
            path = path.split("\\")
        else:
            path = [path]
        return os.path.join(root_path, *path)
    else:
        return root_path


def get_my() -> str:
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


def 返回当前时间xxxx_xx_xx加N天(add_day: int, time_type="使用中划线分隔符"):
    if time_type == "使用斜杠分隔符":
        return (datetime.datetime.now() + datetime.timedelta(days=add_day)).strftime("%Y/%m/%d")
    elif time_type == "使用中划线分隔符":
        return (datetime.datetime.now() + datetime.timedelta(days=add_day)).strftime("%Y-%m-%d")
    elif time_type == "使用datetime格式":
        return datetime.datetime.now() + datetime.timedelta(days=add_day)
    elif time_type == "使用年月日格式":
        return (datetime.datetime.now() + datetime.timedelta(days=add_day)).strftime("%Y年%m月%d日")
    else:
        return (datetime.datetime.now() + datetime.timedelta(days=add_day)).strftime(str(time_type))


def 返回当前日期和减N天的日期(add_day: int, time_type="使用中划线分隔符"):
    if time_type == "使用斜杠分隔符":
        return (datetime.datetime.now() + datetime.timedelta(days=add_day)).strftime("%Y/%m/%d")
    elif time_type == "使用中划线分隔符":
        return (datetime.datetime.now() + datetime.timedelta(days=add_day)).strftime("%Y-%m-%d")
    elif time_type == "使用datetime格式":
        return datetime.datetime.now() + datetime.timedelta(days=add_day)
    elif time_type == "使用年月日格式":
        return datetime.datetime.now().strftime("%Y年%m月%d日"), (datetime.datetime.now() + datetime.timedelta(days=add_day)).strftime("%Y年%m月%d日")
    else:
        return (datetime.datetime.now() + datetime.timedelta(days=add_day)).strftime(str(time_type))


def 将日期中的01月01日替换为1月1日(date: str):
    year, date = date.split('年')
    m, d = date.split('月')
    if m.startswith('0'):
        m = m.replace('0', '')
    if d.startswith('0'):
        d = d.replace('0', '')
    return year + '年' + m + '月' + d


def get_bj_time():
    url = r'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    res_json = requests.get(url).json()
    bj_time = res_json['data']['t']
    bj_time = int(bj_time) / 1000
    return bj_time


def get_bj_time_timetuple():
    bj_time_timetuple = time.gmtime(get_bj_time())
    return bj_time_timetuple


def get_time(minutes, time_type="年月日时分秒"):
    """获取时间"""
    # bj_time = datetime.datetime.fromtimestamp(get_bj_time())
    time_end = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    time_end = time_end.timetuple()
    if time_type == '年月日时分秒':
        time_end = time.strftime("%Y-%m-%d %H:%M:%S", time_end)
    elif time_type == '时分':
        time_end = time.strftime("%H:%M", time_end)
    return str(time_end)


def get_days(date_str):
    if not date_str:
        raise Exception('未获取到开始日期')
    from datetime import datetime
    from datetime import date
    today = date.today().strftime("%Y-%m-%d")
    date_str = date_str
    # 将字符串转换为日期对象
    date1 = datetime.strptime(date_str, "%Y-%m-%d")
    date2 = datetime.strptime(today, "%Y-%m-%d")
    # 计算两个日期之间的天数差
    delta = (date2 - date1).days
    return delta


if __name__ == '__main__':
    # print(将日期中的01日替换为1日('2024年10月02日'))
    print(get_days('2024-11-14'))
