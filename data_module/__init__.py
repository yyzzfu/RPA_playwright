import copy
import random
import re
import time
from utils.tools import get_path, get_my, get_time_now


class As_dict:

    time_str = str(int(time.time()))

    def as_dict(self):
        return_dict = self.__dict__
        return_dict_new = return_dict.copy()
        for k, v in return_dict.items():
            if k.startswith('__'):
                return_dict_new.pop(k)
        return_dict_new_temp = return_dict_new.copy()
        for key, value in return_dict_new_temp.items():
            if isinstance(value, str):
                if "时间戳" in value:
                    value = str(value).replace("+时间戳", self.time_str)
                    return_dict_new.update({key: value})
                elif "随机数" in value:
                    pattern = r'\d+'
                    res = re.findall(pattern, value)
                    value = str(random.randint(*[int(i) for i in res]))
                    return_dict_new.update({key: value})
            elif isinstance(value, dict):
                for k, v in value.items():
                    if "时间戳" in v:
                        v = str(v).replace("+时间戳", self.time_str)
                        return_dict_new[key].update({k: v})
                    elif "随机数" in value:
                        pattern = r'\d+'
                        res = re.findall(pattern, v)
                        v = str(random.randint(*[int(i) for i in res]))
                        return_dict_new[key].update({k: v})

    @classmethod
    def as_dict_class(cls):
        return_dict = cls.__dict__
        return_dict_new = return_dict.copy()
        for k, v in return_dict.items():
            if k.startswith('__'):
                return_dict_new.pop(k)
        return_dict_new_temp = return_dict_new.copy()
        for key, value in return_dict_new_temp.items():
            if isinstance(value, str):
                if "时间戳" in value:
                    value = str(value).replace("+时间戳", cls.time_str)
                    return_dict_new.update({key: value})
                elif "随机数" in value:
                    pattern = r'\d+'
                    res = re.findall(pattern, value)
                    value = str(random.randint(*[int(i) for i in res]))
                    return_dict_new.update({key: value})
            elif isinstance(value, dict):
                for k, v in value.items():
                    if "时间戳" in v:
                        v = str(v).replace("+时间戳", cls.time_str)
                        return_dict_new[key].update({k: v})
                    elif "随机数" in value:
                        pattern = r'\d+'
                        res = re.findall(pattern, v)
                        v = str(random.randint(*[int(i) for i in res]))
                        return_dict_new[key].update({k: v})
        return return_dict_new
