from playwright.sync_api import Page, expect, Browser, BrowserContext

from data_module.my_data import MyData
from module import PageIns
import pytest
import allure

from filelock import FileLock