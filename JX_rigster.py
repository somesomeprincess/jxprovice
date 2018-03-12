import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utils.driver import Driver
from Utils.handle import *
import unittest

class JX_Rigster(unittest.TestCase):
    def setUp(self):

        with open('zhanghao.json', 'r') as f:
            self.user = json.load(f)

        self.driver = Driver('chrome')





    def test_register(self):
        close_popup(self.driver,self.name_json)
        register('admin', 'email@qq.com', '134000000', 'org')

