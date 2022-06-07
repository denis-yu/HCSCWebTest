# -- coding: utf-8 --
# @Time : 6/6/22 9:33 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : hcsc_check_out.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class CheckOutPage:
    def __init__(self, driver: webdriver.Chrome()):
        self.driver = driver
    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".top-nav-items:nth-child(5) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".am-input-group-label:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select-all-event .am-icon-checked").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'结算\')]").click()
        self.driver.find_element(By.LINK_TEXT, "自提点取货").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'选择取货地址\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".extraction-address-item:nth-child(2) > .am-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".memo-input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".memo-input").send_keys("留言1")
        self.driver.find_element(By.XPATH, "//form[contains(.,\'提交订单\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".payment-list > li:nth-child(2)").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'提交订单\')]").click()
        self.driver.find_element(By.LINK_TEXT, "回到首页").click()