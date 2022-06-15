# -- coding: utf-8 --
# @Time : 6/6/22 2:24 PM
# @Project : HCWebTest
# @Author : Denis Yu
# @File : home_page.py
# @Software: PyCharm

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import logging


class HCHomePage:
    def __init__(self):
    #     driver = browser
        vars = []

    """
    登录函数
    """
    def to_login(self,driver):
        driver.get("http://shop-xo.hctestedu.com") #todo 环境变量
        loginLink = driver.find_element(By.LINK_TEXT, "登录")
        loginLink.click()
        accounts = driver.find_element(By.NAME, "accounts")
        accounts.click()
        accounts.send_keys("denis20220501") #todo 数据驱动
        pwd = driver.find_element(By.NAME, "pwd")
        pwd.click()
        pwd.send_keys("1234qwer")
        loginButton = driver.find_element(By.XPATH, "//button[contains(.,\'登录\')]")
        loginButton.click()
        logging.info("进入主页")
        actions = ActionChains(driver)
        actions.move_to_element(loginButton).perform()


    def to_person_center(self,driver):

        personCenter = driver.find_element(By.XPATH, "//span[contains(.,\'个人中心\')]")
        personCenter.click()
        logging.info("进入个人中心")


    def search_product_by_keyword(self,driver,keyword): #todo 数据驱动
        # driver.find_element(By.CSS_SELECTOR, ".nav-search > .am-container").click()
        # driver.find_element(By.ID, "search-input").click()
        # driver.find_element(By.CSS_SELECTOR, ".nav-search > .am-container").click()
        # driver.find_element(By.CSS_SELECTOR, ".nav-search").click()
        keywordInput = driver.find_element(By.CSS_SELECTOR, ".search-hot-keywords")
        keywordInput.click()
        navSearch = driver.find_element(By.CSS_SELECTOR, ".nav-search")
        navSearch.click()
        self.vars["window_handles"] = driver.window_handles
        driver.find_element(By.LINK_TEXT, keyword).click()
        self.vars[1] = driver.wait_for_window(2000)
        self.vars["root"] = driver.current_window_handle
        driver.switch_to.window(self.vars[1])
        driver.switch_to.window(self.vars["root"])
        searchInput=driver.find_element(By.ID, "search-input")
        searchInput.click()
        searchInput.send_keys(keyword)
        searchInput.send_keys(Keys.ENTER)
        driver.find_element(By.ID, "ai-topsearch").click()
        # return ProductDetailPage()
