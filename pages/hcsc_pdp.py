# -- coding: utf-8 --
# @Time : 6/6/22 4:33 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : hcsc_pdp.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from testcases.hcsc_check_out import CheckOutPage


class ProductDetailPage:
    def __init__(self, driver: webdriver.Chrome()):
        self.driver = driver
        self.vars = {}
    def addToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".map-images-text-items li:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".screening-price-container .map-more-submit").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".goods-params-container li:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".am-nbfc > .active:nth-child(1)").click()
        self.driver.execute_script("window.scrollTo(0,302)")
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.implicitly_wait(500)
        self.driver.find_element(By.CSS_SELECTOR, ".goods-images").click()
        self.vars[1] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars[1])
        self.driver.find_element(By.ID, "add").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\' 加入购物车\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sku-line:nth-child(2) > img").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\' 加入购物车\')]").click()
        return CheckOutPage(self.driver)