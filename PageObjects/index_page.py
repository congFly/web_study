from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


# 首页
class IndexPage:
    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        # self.driver = driver

    def isExit_quitEle(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
                (By.XPATH, '//span/a[text()="退出"]')))
            return True
        except:
            return False

    # 选择标
    def click_firstBid(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-special"]')))
        self.driver.find_element_by_xpath('//a[@class="btn btn-special"]').click()
