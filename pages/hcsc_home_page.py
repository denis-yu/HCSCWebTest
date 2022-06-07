# -- coding: utf-8 --
# @Time : 6/6/22 2:24 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : hcsc_home_page.py
# @Software: PyCharm
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from pages.hcsc_pdp import ProductDetailPage
from pages.hcsc_person_center_page import PersonCenterPage


class HCHomePage:
    # def __init__(self,openbrowser):
    #     driver = opendriver
    #     vars = {}

    def to_login(driver):
        driver.get("http://shop-xo.hctestedu.com")
        loginLink = driver.find_element(By.LINK_TEXT, "登录")
        loginLink.click()
        accounts = driver.find_element(By.NAME, "accounts")
        accounts.click()
        accounts.send_keys("denis20220501")
        pwd = driver.find_element(By.NAME, "pwd")
        pwd.click()
        pwd.send_keys("1234qwer")
        loginButton = driver.find_element(By.XPATH, "//button[contains(.,\'登录\')]")
        loginButton.click()
        actions = ActionChains(driver)
        actions.move_to_element(loginButton).perform()

    def to_person_center(driver):
        personCenter = driver.find_element(By.XPATH, "//span[contains(.,\'个人中心\')]")
        personCenter.click()
        return PersonCenterPage(driver)

    def search_product_by_keyword(driver):
        driver.find_element(By.CSS_SELECTOR, ".nav-search > .am-container").click()
        driver.find_element(By.ID, "search-input").click()
        driver.find_element(By.CSS_SELECTOR, ".nav-search > .am-container").click()
        driver.find_element(By.CSS_SELECTOR, ".nav-search").click()
        driver.find_element(By.CSS_SELECTOR, ".search-hot-keywords").click()
        driver.find_element(By.CSS_SELECTOR, ".nav-search").click()
        vars["window_handles"] = driver.window_handles
        driver.find_element(By.LINK_TEXT, "连衣裙").click()
        vars[1] = driver.wait_for_window(2000)
        vars["root"] = driver.current_window_handle
        driver.switch_to.window(vars[1])
        driver.switch_to.window(vars["root"])
        driver.find_element(By.ID, "search-input").click()
        driver.find_element(By.ID, "search-input").send_keys("连衣裙")
        driver.find_element(By.ID, "search-input").send_keys(Keys.ENTER)
        driver.find_element(By.ID, "ai-topsearch").click()
        return ProductDetailPage(driver)
