import json
import os
from filelock import FileLock

from utils.tools import get_path


class GlobalMap:
    """文件全局变量，为了进程间能通讯"""

    def __init__(self, file_path=".Auth/data.json"):
        self.temp_lock_path = get_path(".Auth/temp.lock")
        self.data_json_path = get_path(file_path)

        os.makedirs(os.sep.join(self.data_json_path.split(os.sep)[:-1]), exist_ok=True)
        with FileLock(self.temp_lock_path):
            file_exists = os.path.exists(self.data_json_path)
            if not file_exists:
                with open(self.data_json_path, "w") as f:
                    json.dump({}, f)

    def __load(self):
        with open(self.data_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def __dump(self, data):
        with open(self.data_json_path, "w", encoding='utf-8') as f:
            json.dump(data, f)

    def set(self, key, value):
        with FileLock(self.temp_lock_path):
            data = self.__load()
            data[key] = value
            self.__dump(data)

    def get(self, key, default=None):
        with FileLock(self.temp_lock_path):
            data = self.__load()
            return data.get(key, default)

    def delete(self, key):
        with FileLock(self.temp_lock_path):
            data = self.__load()
            data.pop(key)
            self.__dump(data)

    def get_all(self):
        with FileLock(self.temp_lock_path):
            data = self.__load()
            return data.items()

    def set_all(self, **kwargs):
        with FileLock(self.temp_lock_path):
            data = self.__load()
            data.updata(**kwargs)
            self.__dump(data)


if __name__ == '__main__':
    GlobalMap().set('key', 'haha111')
    GlobalMap().set('key2', 'haha2')