import os
import time
import random
import datetime

import requests


def get_path(path: str) -> str:
    if path[0] != "/":
        path = f"/{path}"
    return f"{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}{path}"


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


def get_bj_time():
    url = r'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    res_json = requests.get(url).json()
    bj_time = res_json['data']['t']
    bj_time = int(bj_time) / 1000
    return bj_time


def get_bj_time_timetuple():
    bj_time_timetuple = time.gmtime(get_bj_time())
    return bj_time_timetuple


def get_time(minutes):
    """获取时间"""
    bj_time = datetime.datetime.fromtimestamp(get_bj_time())
    time_end = bj_time + datetime.timedelta(minutes=minutes)
    time_end = time_end.timetuple()
    time_end = time.strftime("%Y-%m-%d %H:%M:%S", time_end)
    return time_end


if __name__ == '__main__':
    print(get_time.__doc__)
