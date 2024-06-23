import os
import time
import random


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


if __name__ == '__main__':
    print(get_path('1.png'))
