from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BidPage:
    def __init__(self, driver):
        self.driver = driver
    # 获取用户余额
    def get_userLeftMoney(self):
        pass

    # 投资操作
    def invest(self, money):
        pass

    # 投资成功弹出框/点击查看并激活
    def click_activeButton_on_investSuccess_popup(self):
        pass
