# -- coding: utf-8 --
# @Time : 6/6/22 2:51 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : hcsc_person_center_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By

class PersonCenterPage:
    def __init__(self, driver: webdriver.Chrome()):
        self.driver = driver
    def toOrderManager(self):
        orderManager=self.driver.find_element(By.LINK_TEXT, "订单管理")
        orderManager.click()

    def toinfoManager(self):
        infoManager=self.driver.find_element(By.LINK_TEXT, "资料管理")
        infoManager.click()