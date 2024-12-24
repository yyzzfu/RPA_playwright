from playwright.sync_api import Page, expect, Browser, BrowserContext

from data_module.WeCom_workbench_data import CreateGroupData, SendMsgData
from data_module.fast_task_data import FastData
from data_module.gaoji_task_data import GaoJiGroupData, GaoJiPersonData, GaoJiNoticeData, GaoJiGroupDataOneByOne, \
    GaoJiGroupDataAllGroup
from data_module.group_rename_task_data import GroupRenameData, GroupRenameRegularData
from data_module.jisu_task_data import JiSuPersonData, JiSuGroupData
from data_module.muban_data import MuBanData
from data_module.user_data import UserData
from data_module.train_camp_data import TrainCampGaoJiGroupData, TrainCampGaoJiPersonData, TrainCampGaoJiNoticeData, \
    TrainCampGaoJiGroupDataOneByOne, TrainCampJiSuGroupData, TrainCampJiSuPersonData, TrainCampGaoJiPersonData_2, \
    TrainCampVoiceData, TrainCampVoiceData_2
from module import PageIns
import pytest
import allure

from filelock import FileLock
from data_module.pull_group_task_data import PullGroupData