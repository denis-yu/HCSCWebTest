# -- coding: utf-8 --
# @Time : 6/6/22 2:51 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : person_center_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class PersonCenterPage:

    def to_order_manager(self,driver):
        driver.implicitly_wait(500)
        orderManager = driver.find_element(By.LINK_TEXT, "订单管理")
        orderManager.click()

    def to_info_manager(self,driver):
        driver.implicitly_wait(500)
        infoManager = driver.find_element(By.LINK_TEXT, "资料管理")
        infoManager.click()
