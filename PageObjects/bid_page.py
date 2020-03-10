from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BidPage:
    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        # self.driver = driver

    # 获取用户余额
    def get_userLeftMoney(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@class='color_sub']")))
        print(self.driver.find_element_by_xpath("//li[@class='color_sub']").text)
        return self.driver.find_element_by_xpath("//li[@class='color_sub']").text

    # 投资操作
    def invest(self, money):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//button[text()="投标"]')))
        self.driver.find_element_by_xpath("//div/input[@class='form-control invest-unit-investinput']").send_keys(money)
        self.driver.find_element_by_xpath('//button[text()="投标"]').click()

    # 投资成功弹出框/点击查看并激活
    def click_activeButton_on_investSuccess_popup(self):
        WebDriverWait(self.driver, 20).until(
            (By.XPATH, "//div[@class='layui-layer-content']//button[text()='查看并激活']"))
        self.driver.find_element_by_xpath("//div[@class='layui-layer-content']//button[text()='查看并激活']").click()

    # 输入金额不是10的整数
    def invest_no10_Failed(self):
        WebDriverWait(self.driver, 20).until(
            (By.XPATH, "//button[@class='btn btn-special height_style']"))
        return self.driver.find_element_by_xpath("//button[@class='btn btn-special height_style']").text
