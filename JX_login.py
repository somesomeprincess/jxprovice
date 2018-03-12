import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils.handle import *
from Utils.driver import Driver
import unittest

class JXLogin(unittest.TestCase):
    def setUp(self):
        jx_url = 'http://ywgl.jxstc.gov.cn/egrantweb/'
        self.driver = Driver('chrome')

        self.driver.implicitly_wait(10)
        open_url(jx_url)
        self.driver.maximize_window()

    def test_loginsuccess(self):

        close_the_tishi(self.driver)
        login(self.driver,'admin','123456')
        title=self.driver.title
        self.assertEqual(title,'江西省科技业务综合管理系统|爱瑞思科技管理系统(IRISaaS) -  登录')

    def test_loginfail_usrwrong(self):
        close_the_tishi(self.driver)
        login(self.driver, 'admin1', '123456')
        tishi = self.driver.find_element(By.CSS_SELECTOR, 'p[style="color:red;"]').text
        self.assertEqual(tishi,' 您输入的用户名或密码有误，请重新输入.')

    def test_loginfail_usrnull(self):
        close_the_tishi(self.driver)
        login(self.driver, '', '123456')
        tishi = self.driver.find_element(By.CSS_SELECTOR, 'p[style="color:red;"]').text
        self.assertEqual(tishi,' 您输入的用户名或密码有误，请重新输入.')

    def test_loginfail_pwdwrong(self):
        close_the_tishi(self.driver)
        login(self.driver, 'admin', '111111')
        tishi = self.driver.find_element(By.CSS_SELECTOR, 'p[style="color:red;"]').text
        self.assertEqual(tishi,' 您输入的用户名或密码有误，请重新输入.')

    def test_loginfail_pwdnull(self):
        close_the_tishi(self.driver)
        login(self.driver, 'admin', '')
        tishi = self.driver.find_element(By.CSS_SELECTOR, 'p[style="color:red;"]').text
        self.assertEqual(tishi,' 您输入的用户名或密码有误，请重新输入.')



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()