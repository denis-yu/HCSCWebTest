# -- coding: utf-8 --
# @Time : 6/6/22 6:33 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : browser.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class browser:
    driver: webdriver = None

    def __init__(self):
        self.vars = None

    def start(self):
        caps = Options()
        caps.add_argument('--no-sandbox')
        caps.add_argument('--disable-dev-shm-usage')
        caps.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=caps)
        self.vars = {}

    def close(self):
        self.driver.quit()