# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class HPDental(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_h_p_dental(self):
        driver = self.driver
        driver.get("https://pengujian.healthpocket.com/")
        driver.find_element_by_xpath("//div[@id='hpHero']/div/div").click()
        driver.find_element_by_xpath("//div[@id='hpHero']/div/div").click()
        driver.find_element_by_id("location").clear()
        driver.find_element_by_id("location").send_keys("30301")
        driver.find_element_by_link_text("30301 - Fulton County, GA").click()
        driver.find_element_by_id("planTypeDropdown").click()
        driver.find_element_by_xpath("//div[@id='changeProductLine']/div/ul/li[3]/a").click()
        driver.find_element_by_id("findPlans").click()
        driver.find_element_by_xpath("//div[@id='js-census-bar']/div/div/div[2]/div[2]/ul/li[4]/button").click()
        driver.find_element_by_id("js-census-backdrop").click()
        driver.find_element_by_xpath("//div[@id='js-census-bar']/div/div/div[2]/div[2]/ul/li[2]/button").click()
        driver.find_element_by_xpath("//div[@id='js-filter-company-popover']/form/div/div/ul/li[2]/div/div/div/label").click()
        driver.find_element_by_xpath("//div[@id='js-filter-company-popover']/form/button[2]").click()
        driver.find_element_by_link_text("Select").click()
        driver.find_element_by_xpath("//div[@id='js-details']/div/div/div/div[4]/div/div[2]/div[2]/div/div/div/a").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.get("https://praetemptatus.agilehealthinsurance.com/dental-insurance-quotes?utm_source=healthpocket&utm_medium=detail_page&utm_campaign=dental_detail_page_xsell&_ga=2.267067213.2133460297.1654264917-1115045339.1640574889&census[location][zip]=30301")
        driver.find_element_by_id("i-zip").click()
        driver.find_element_by_id("i-zip").clear()
        driver.find_element_by_id("i-zip").send_keys("30302")
        driver.find_element_by_id("i-zip").clear()
        driver.find_element_by_id("i-zip").send_keys("30301")
        driver.find_element_by_id("i-member.0.dob").click()
        driver.find_element_by_id("i-member.0.dob").clear()
        driver.find_element_by_id("i-member.0.dob").send_keys("03/19/1990")
        driver.find_element_by_xpath("//div[@id='__next']/div/div/div/div[2]/div/div/form/div[2]/div/div[2]/div[2]/span/button").click()
        driver.find_element_by_xpath("//div[@id='__next']/div/div/div/div[2]/div/div/form/button").click()
        driver.get("https://praetemptatus.agilehealthinsurance.com/dental-insurance/quote")
        driver.find_element_by_xpath("//div[@id='__next']/div/div/div/div[2]/div[5]/div[2]/div/div/div/div[2]/div[2]/button/span").click()
        driver.get("https://praetemptatus.agilehealthinsurance.com/dental-insurance/plan/united-concordia-protector-ga")
        driver.find_element_by_id("plan-details-primary-apply").click()
        driver.get("https://praetemptatus.agilehealthinsurance.com/dental-insurance/apply/united-concordia-protector-ga")
        driver.find_element_by_xpath("//a[@id='applyButton']/span[3]").click()
        driver.get("https://praetemptatus.agilehealthinsurance.com/dental-insurance/application/test-united-concordia-ga-u8cwohebxl")
        driver.find_element_by_id("fillApp").click()
        driver.find_element_by_id("js-app-continue-link").click()
        driver.find_element_by_xpath("//div[@id='credit-authorization']/div/div/div/label").click()
        driver.find_element_by_id("js-app-continue-link").click()
        driver.find_element_by_xpath("//div[@id='js-consent-review']/div/div/div/div/div/label").click()
        driver.find_element_by_xpath("//div[@id='js-signature-tab']/span").click()
        driver.find_element_by_id("js-app-continue-link").click()
        driver.find_element_by_xpath("//div[@id='app-confirmation']/div/h2").click()
        driver.find_element_by_xpath("//div[@id='app-confirmation']/div").click()
        driver.find_element_by_xpath("//div[@id='app-confirmation']/div/h2/span").click()
        try: self.assertEqual("Thank You. Your application has been submitted!", driver.find_element_by_xpath("//div[@id='app-confirmation']/div/h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
