import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from selenium import webdriver


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # 登录成功
    def test_login_success(self):
        # 步骤：登录页面的登录功能+用户信息查询
        LoginPage(self.driver).login('18829291885', '123456fly')

        # 断言：用户信息查询
        self.assertTrue(IndexPage(self.driver).isExit_quitEle())

    # 登录失败-没有密码
    def test_login_noPasswd(self):
        # 步骤：登录页面的登录功能+用户信息查询
        lp = LoginPage(self.driver)
        lp.login('18829291885', '')
        # 断言：错误提示信息是否正确
        self.assertEqual("请输入密码", lp.get_errorMsg_from_loginArea())

    def test_login_noUser(self):
        # 步骤：登录页面的登录功能+用户信息查询
        lp = LoginPage(self.driver)
        lp.login('', '123456fly')
        # 断言：错误提示信息是否正确
        self.assertEqual("请输入手机号", lp.get_errorMsg_from_loginArea())

    def test_login_UserLess11(self):
        # 步骤：登录页面的登录功能+用户信息查询
        lp = LoginPage(self.driver)
        lp.login('1882929188', '123456fly')
        # 断言：错误提示信息是否正确
        self.assertEqual("请输入正确的手机号", lp.get_errorMsg_from_loginArea())
