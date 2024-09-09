import random
import re

from data_module.user_data import UserData
from utils.tools import get_path, get_my, get_time_now


class As_dict:

    def as_dict(self, kf_for_data=None):
        time_str = get_time_now()
        return_dict = self.__dict__
        return_dict_new = return_dict.copy()
        for k, v in return_dict.items():
            if k.startswith('__'):
                return_dict_new.pop(k)
        return_dict_new_temp = return_dict_new.copy()
        for key, value in return_dict_new_temp.items():
            if isinstance(value, str):
                if "时间戳" in value:
                    value = str(value).replace("+时间戳", time_str)
                    return_dict_new.update({key: value})
                if "随机数" in value:
                    pattern = r'\d+'
                    res = re.findall(pattern, value)
                    value = str(random.randint(*[int(i) for i in res]))
                    return_dict_new.update({key: value})
                if "名人名言" in value:
                    value = str(value).replace("+名人名言", get_my())
                    return_dict_new.update({key: value})
                if "企微账号" in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('wechat_name_list')})
                if '群发对象-按客户' in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('send_customer_list')})
                if '群发对象-指定群' in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('send_group_list')})
                if '智能助理' in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('agent')})
            elif isinstance(value, dict):
                for k, v in value.items():
                    if "时间戳" in v:
                        v = str(v).replace("+时间戳", time_str)
                        return_dict_new[key].update({k: v})
                    if "随机数" in value:
                        pattern = r'\d+'
                        res = re.findall(pattern, v)
                        v = str(random.randint(*[int(i) for i in res]))
                        return_dict_new[key].update({k: v})
                    if "名人名言" in value:
                        value = str(value).replace("+名人名言", get_my())
                        return_dict_new.update({key: value})

    @classmethod
    def as_dict_class(cls, kf_for_data=None):
        time_str = get_time_now()
        return_dict = cls.__dict__
        return_dict_new = return_dict.copy()
        for k, v in return_dict.items():
            if k.startswith('__'):
                return_dict_new.pop(k)
        return_dict_new_temp = return_dict_new.copy()
        for key, value in return_dict_new_temp.items():
            if isinstance(value, str):
                if "时间戳" in value:
                    value = str(value).replace("+时间戳", time_str)
                    return_dict_new.update({key: value})
                if "随机数" in value:
                    pattern = r'\d+'
                    res = re.findall(pattern, value)
                    value = str(random.randint(*[int(i) for i in res]))
                    return_dict_new.update({key: value})
                if "名人名言" in value:
                    value = str(value).replace("+名人名言", get_my())
                    return_dict_new.update({key: value})
                if "企微账号" in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('wechat_name_list')})
                if "企微账号" in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('wechat_name_list')})
                if '群发对象-按客户' in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('send_customer_list')})
                if '群发对象-指定群' in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('send_group_list')})
                if '智能助理' in value:
                    return_dict_new.update({key: UserData().data_for_test(kf_for_data).get('agent')})
            elif isinstance(value, dict):
                for k, v in value.items():
                    if "时间戳" in v:
                        v = str(v).replace("+时间戳", time_str)
                        return_dict_new[key].update({k: v})
                    if "随机数" in value:
                        pattern = r'\d+'
                        res = re.findall(pattern, v)
                        v = str(random.randint(*[int(i) for i in res]))
                        return_dict_new[key].update({k: v})
                    if "名人名言" in value:
                        v = str(v).replace("+名人名言", time_str)
                        return_dict_new[key].update({k: v})
        return return_dict_new
