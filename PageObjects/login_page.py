from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PageLocators.loginPage_locator import LoginPageLocator as loc


class LoginPage:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 登录功能
    def login(self, username, passwd):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.user_passwd))
        self.driver.find_element(*loc.user_input).send_keys(username)
        self.driver.find_element(*loc.user_passwd).send_keys(passwd)
        self.driver.find_element(*loc.login_button).click()

    # 获取错误提示-没有密码-登录框区域提示
    def get_errorMsg_from_loginArea(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(loc.errorMsg_from_loginArea))
        return self.driver.find_element(*loc.errorMsg_from_loginArea).text

    # 获取错误提示-密码错误-页面中间提示
    def get_errorMsg_from_pageCenter(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(loc.errorMsg_from_pageCenter))
        return self.driver.find_element(*loc.errorMsg_from_pageCenter).text
