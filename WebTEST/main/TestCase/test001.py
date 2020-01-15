#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test001.py
# @Time      :2020/1/11 14:56
# @Author    :ZhouYue
# @Description    :

import unittest,json,time, traceback
from main.commom.tools.log import log
import main.pages.LoginPage as login
import warnings
from main.commom.init.Browser import Browser
# from common.keywords import decorator


class Login(unittest.TestCase):
    """云台控制：云台旋转"""

    logs = log.Log()
    logger = logs.getlog()

    @classmethod
    def setUpClass(cls):
        """终端鉴权上线"""
        warnings.simplefilter("ignore", ResourceWarning)
        Login.logger.info(u"【***********START TEST***********】")

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        Login.logger.info(u"【***********END TEST***********】")

    def test_01(self):
        """case_id:1"""
        loginPage = login.loginPage()
        loginPage.login("18502827849", "123456")
        shouye = loginPage.findElementByJQuery("div[title='首页']")
        loginPage.quit()
        self.assertIsNotNone(shouye)

    def test_02(self):
        """case_id:2"""
        Browser().setDriver()
        loginPage = login.loginPage()
        loginPage.login("18502827849", "123456")
        shixiang = loginPage.findElementByJQuery("div[title='我的事项']")
        loginPage.quit()
        self.assertIsNotNone(shixiang)


if __name__=='__main__':
    #执行所有用例
    unittest.main()


