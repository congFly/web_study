from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 登录功能
    def login(self, username, passwd):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(By.XPATH("//input[@name='phone']")))
        self.driver.find_element_by_xpath('//input[@name="phone"]').send_keys(username)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//button').click()

    # 获取错误提示-没有密码
    def get_errorMsg_noPasswd(self):
        pass
