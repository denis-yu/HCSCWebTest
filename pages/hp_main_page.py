# -- coding: utf-8 --
# @Time : 6/4/22 10:43 AM
# @Project : HPWebTest
# @Author : Denis Yu
# @File : hp_main_page.py
# @Software: PyCharm
from selenium import webdriver

from pages.hp_medicare_quote_page import HPMedicareQuotePage


class HPMainPage:
    def __init__(self, driver: webdriver.Chrome()):
        self.driver = driver
        self.driver.get("https://pengujian.healthpocket.com/")

    def toProductLine(self):
        location = self.driver.find_element_by_id("location")
        location.click()
        location.clear()
        location.send_keys("60601")
        address = self.driver.find_element_by_link_text("60601 - Cook County, IL")
        address.click()
        plDropdown = self.driver.find_element_by_xpath("//a[@id='planTypeDropdown']/span")
        plDropdown.click()
        plSelection = self.driver.find_element_by_xpath("//*[@class='c-home-plantype__dropdown-item']/a[contains(text(),'Medicare Insurance')]")
        plSelection.click()
        findPlan = self.driver.find_element_by_id("findPlans")
        findPlan.click()
        return HPMedicareQuotePage(self.driver)
