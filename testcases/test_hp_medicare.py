# -- coding: utf-8 --
# @Time : 6/4/22 11:59 AM
# @Project : HPWebTest
# @Author : Denis Yu
# @File : test_hp_medicare.py.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest, time, re, allure

from pages.hp_main_page import HPMainPage
from pages.hp_medicare_quote_page import HPMedicareQuotePage


class Test_HP_Medicare():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://pengujian.healthpocket.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_hp_medicare(self):
        HPMainPage(self.driver).toProductLine
        HPMedicareQuotePage(self.driver).filterPlan
        HPMedicareQuotePage(self.driver).comparePlans
    #     driver = self.driver
    #     driver.get("https://pengujian.healthpocket.com/")
    #     driver.find_element_by_id("location").click()
    #     driver.find_element_by_id("location").clear()
    #     driver.find_element_by_id("location").send_keys("60601")
    #     driver.find_element_by_link_text("60601 - Cook County, IL").click()
    #     driver.find_element_by_xpath("//a[@id='planTypeDropdown']/span").click()
    #     driver.find_element_by_xpath("//div[@id='changeProductLine']/div/ul/li[4]/a").click()
    #     driver.find_element_by_id("findPlans").click()
    #     driver.find_element_by_xpath("//div[@id='js-census-bar']/div/div/div[2]/div[2]/ul/li[4]/button").click()
    #     driver.find_element_by_xpath("//div[@id='js-filter-more-popover']/form/div/div/ul/li[2]/div/label").click()
    #     driver.find_element_by_xpath("//div[@id='js-filter-more-popover']/form/button[2]").click()
    #     driver.find_element_by_name("compare").click()
    #     driver.find_element_by_xpath("//div[@id='js-plans']/ul/li[2]/div/div[2]/div[2]/input").click()
    #     driver.find_element_by_xpath("//div[@id='js-plans']/ul/li[3]/div/div[2]/div[2]/input").click()
    #     driver.find_element_by_xpath("//div[@id='save-to-compare-plan-header']/div[3]/a/span").click()
    #     driver.find_element_by_xpath("//div[@id='savedPlansPlanContainer']/table/tbody/tr[6]/td[2]/a/span").click()
    #     # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
    #     driver.find_element_by_xpath("//div[@id='js-details']/div/div/div/div[4]/div/div/div/div/div/h1").click()
    #     planName = driver.find_element_by_xpath("//div[@id='js-details']/div/div/div/div[4]").text

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
            pytest.main(['-s', '-r', 'test_hp_medicare.py'])