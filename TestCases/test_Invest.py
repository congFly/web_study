# 1.用例列出=前置/步骤/断言
# 2.明确有哪些页面
"""
用例1.成功投资场景
前置：
1.登录成功状态
2.可用余额应该大于你要投资的金额：1000
  如何保证在自动化的运行过程中，余额可用
    1)充值一笔：33：每次充投资的金额-1000：——利用接口直接充值
    2）暂时充一大笔钱
    3）判断当前用户的余额是否大于投资金额，如果小于，就充值一大笔；如果大于，不用处理——利用接口
       查数据库？网页获取？接口获取？
3.有可投资的标 ——在页面就可辨别标是否可投资——利用元素定位
    1）新建一个标，并且将标置为竞标状态。——接口
    2）达到1）很复杂


投资失败的场景：
1.非100的整数倍
2.非10的整数倍
3.小数点-非数字-负数
4.投资的金额 > 标当前可投的金额（4万）  标+用户的金额同时满足特殊条件
5.投资的金额（5万）> 账户可用余额（2万）
"""
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage
from PageObjects.index_page import IndexPage
from selenium import webdriver
from TestDatas import common_datas as CD
from TestDatas import invest_datas as TD


class TestInvest(unittest.TestCase):
    # def setUpClass(cls):
    #     # 可投资的标？
    #     pass

    def setUp(self):
        # 调用页面对象
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(CD.login_url)
        self.LoginPage(self.driver).login(CD.login_url, CD.password)

    def tearDown(self):
        self.driver.quit()

    def test_invest_success(self):
        #     步骤：
        # 1.首页-选标
        IndexPage(self.driver).click_firstBid()
        # 2.标页面-输入金额，进行投资
        bp = BidPage(self.driver)
        #     2.0 标页面获取当前余额
        userMoney_beforeInvest = bp.get_userLeftMoney()
        bp.invest(TD.money)
        # 3.标页面-投资成功的弹出框中，点击  查看并激活
        bp.click_activeButton_on_investSuccess_popup()
        # 断言：
        #   1.投资前的金额-现在的余额=投资的金额
        #     1.0个人页面获取用户可用余额
        #     2.0-1.0=投资的金额
        userMoney_afterInvest = UserPage(self.driver).get_userLeftMoney()
        investMoney = userMoney_beforeInvest - userMoney_afterInvest
        self.assertEqual(investMoney, TD.money)

    def test_invest_failed_no10(self):
        IndexPage(self.driver).click_firstBid()
        invest_no10_Failed = BidPage(self.driver).invest_no10_Failed(TD.no10_money)
        # 断言
        self.assertEqual("请输入10的整数倍", invest_no10_Failed)
