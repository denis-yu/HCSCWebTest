# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Medicarecoveragehelpline(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_medicarecoveragehelpline(self):
        driver = self.driver
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("zip").click()
        driver.find_element_by_id("zip").clear()
        driver.find_element_by_id("zip").send_keys("60601")
        driver.find_element_by_xpath("//div[@id='__next']/div[2]/div/form/div/div/div/div/div/div/div[2]/button").click()
        driver.find_element_by_id("firstName").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("Test")
        driver.find_element_by_id("lastName").click()
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("last")
        driver.find_element_by_xpath("//div[@id='__next']/div[2]/div/form/div/div/div/div/div/div/div[2]/button").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("testlast@gmail.com")
        driver.find_element_by_xpath("//div[@id='__next']/div[2]/div/form/div/div/div/div/div/div/div[2]/button").click()
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("(344) 334-4334")
        driver.find_element_by_xpath("//div[@id='__next']/div[2]/div/form/div/div/div/div/div/div/div[2]/button").click()
        driver.get("https://staging.medicare.healthinsurance.com/fastQuote?affiliate=mch&tfn=800-976-6274&hours=Mon.-Fri.%208a.m.%20-%208p.m.%20ET&ctx_utm_medium=redirect&ctx_utm_source=mch&zip=60601&_ga=2.267749902.1660669684.1652781091-1464481489.1651745353")
        driver.get("https://staging.medicare.healthinsurance.com/preferences?affiliate=mch&tfn=800-976-6274&hours=Mon.-Fri.%208a.m.%20-%208p.m.%20ET&ctx_utm_medium=redirect&ctx_utm_source=mch&zip=60601&_ga=2.267749902.1660669684.1652781091-1464481489.1651745353")
        driver.find_element_by_xpath("//div[@id='__next']/div[4]/div/div/div[3]/button[2]/div/p").click()
        driver.get("https://staging.medicare.healthinsurance.com/quote")
        driver.find_element_by_id("checkbox-1").click()
        driver.find_element_by_xpath("//div[@id='__next']/div[5]/div/div/div/div/div[3]/div[2]/div/div[7]/button[2]/div/strong/span").click()
        driver.get("https://staging.medicare.healthinsurance.com/preenroll/220255")
        try: self.assertEqual(u"Congratulations on your plan selection! We’re happy to get you enrolled in this plan.", driver.find_element_by_xpath("//div[@id='__next']/div[4]/div/div/div[2]/div/h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='header-top-container']/div/div[2]/div[3]/div[2]/button/div/strong").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('Save your profile information so you don', \"'\", 't lose your work.')])[1]/following::span[1]").click()
        driver.find_element_by_css_selector("div.sc-1n28te6-0.sc-1n28te6-3.kUnSKw > span.sc-1y1e3lq-0.evHsEi > svg > g > g > g > g > path").click()
        try: self.assertEqual("additional information", driver.find_element_by_xpath("//div[@id='__next']/div[4]/div/div/div[3]/div/div/div[2]/div/div/div/div[3]/strong").text)
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
