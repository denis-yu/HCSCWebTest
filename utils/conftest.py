# -- coding: utf-8 --
# @Time : 6/6/22 6:33 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : browser.py
# @Software: PyCharm
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver: webdriver = None


@pytest.fixture(scope='session', autouse=True)
def browser():
    # 前置
    caps = Options()
    caps.add_argument('--no-sandbox')
    caps.add_argument('--disable-dev-shm-usage')
    # caps.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=caps)
    yield driver #yield之前代码是前置，之后的代码就是后置(第二次调用执行)。
    # 后置
    driver.quit()

def close(self):
    driver.quit()
