#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :testBase.py
# @Time      :2020/1/11 14:59
# @Author    :ZhouYue
# @Description    :测试用例基础设置，每个测试用例均继承该类

import unittest,json,time, traceback
import warnings
from main.commom.init.Browser import Browser
from main.commom.base.BasicPage import BasicPage

class testBase(unittest.TestCase,BasicPage):
    """
    测试用例基础设置
    """

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        testBase.logger.info(u"【**********************TEST START**********************】")

    @classmethod
    def tearDownClass(cls):
        testBase.logger.info(u"【**********************TEST END**********************】")

    def setUp(self):
        Browser().setDriver()

    def tearDown(self):
        Browser.driver.quit()


if __name__=='__main__':
    #执行所有用例
    unittest.main()


