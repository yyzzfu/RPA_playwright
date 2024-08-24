from playwright.sync_api import Page, expect, Browser, BrowserContext

from data_module.mydata import MyData
from module import PageIns
import pytest
from filelock import FileLock