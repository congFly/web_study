from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class UserPage:
    def __init__(self, driver):
        self.driver = driver

    # 获取投资后的余额
    def get_userLeftMoney(self):
        pass
