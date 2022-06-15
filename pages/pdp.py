# -- coding: utf-8 --
# @Time : 6/6/22 4:33 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : pdp.py
# @Software: PyCharm
import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from testcases.test_check_out import CheckOutPage


class ProductDetailPage:
    def __init__(self):
    #    driver = driver
       vars = []
    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def addToCart(self,driver):
       logging.info("进入详情页面")
       driver.find_element(By.CSS_SELECTOR, ".map-images-text-items li:nth-child(2)").click()
       driver.find_element(By.CSS_SELECTOR, ".screening-price-container .map-more-submit").click()
       driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
       driver.find_element(By.CSS_SELECTOR, ".goods-params-container li:nth-child(1)").click()
       driver.find_element(By.CSS_SELECTOR, ".am-nbfc > .active:nth-child(1)").click()
       driver.execute_script("window.scrollTo(0,302)")
       self.vars["window_handles"] =driver.window_handles
       driver.implicitly_wait(500)
       driver.find_element(By.CSS_SELECTOR, ".goods-images").click()
       self.vars[1] = self.wait_for_window(2000)
       driver.switch_to.window(self.vars[1])
       driver.find_element(By.ID, "add").click()
       driver.find_element(By.XPATH, "//button[contains(.,\' 加入购物车\')]").click()
       driver.find_element(By.CSS_SELECTOR, ".sku-line:nth-child(2) > img").click()
       driver.find_element(By.XPATH, "//button[contains(.,\' 加入购物车\')]").click()
       logging.info("加完购物车，进入订单页面")
        # return CheckOutPage(self.driver)