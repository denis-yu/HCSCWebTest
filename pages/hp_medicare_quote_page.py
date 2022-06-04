# -- coding: utf-8 --
# @Time : 6/4/22 11:14 AM
# @Project : HPWebTest
# @Author : Denis Yu
# @File : hp_medicare_quote_page.py
# @Software: PyCharm
from selenium import webdriver


class HPMedicareQuotePage:
    def __init__(self, driver):
        self.driver = driver

    def filterPlan(self):
        filterPlan = self.driver.find_element_by_xpath(
            "//div[@id='js-census-bar']/div/div/div[2]/div[2]/ul/li[4]/button")
        filterPlan.click()
        healthAndDrug = self.driver.find_element_by_xpath(
            "//div[@id='js-filter-more-popover']/form/div/div/ul/li[2]/div/label")
        healthAndDrug.click()
        showPlans = self.driver.find_element_by_xpath("//div[@id='js-filter-more-popover']/form/button[2]")
        showPlans.click()

    def comparePlans(self):
        plan1 = self.driver.find_element_by_xpath("//div[@id='js-plans']/ul/li[2]/div/div[2]/div[2]/input")
        plan1.click()
        plan2 = self.driver.find_element_by_xpath("//div[@id='js-plans']/ul/li[3]/div/div[2]/div[2]/input")
        plan2.click()
        plan3 = self.driver.find_element_by_xpath("//div[@id='save-to-compare-plan-header']/div[3]/a/span")
        plan3.click()
        compareButton = self.driver.find_element_by_xpath(
            "//div[@id='savedPlansPlanContainer']/table/tbody/tr[6]/td[2]/a/span")
        compareButton.click()
