from playwright.sync_api import Page, expect, Browser, BrowserContext

from data_module.fast_task_data import FastData
from data_module.gaoji_task_data import GaoJiGroupData, GaoJiPersonData, GaoJiNoticeData, GaoJiGroupDataOneByOne
from data_module.group_rename_task_data import GroupRenameData, GroupRenameRegularData
from data_module.jisu_task_data import JiSuPersonData, JiSuGroupData
from data_module.muban_data import MuBanData
from data_module.user_data import UserData
from module import PageIns
import pytest
import allure

from filelock import FileLock
from data_module.pull_group_task_data import PullGroupData