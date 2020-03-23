#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test001_login.py
# @Time      :2020/1/11 14:56
# @Author    :ZhouYue
# @Description    :

import unittest
import main.commom.base.testBase as testBase
import main.pages.LoginPage as login
import main.pages.MainPage as Main
from main.commom.tools import decorator

class Login(testBase.testBase):
    """登录测试"""

    @decorator.Call_CaseName("【正确登录】用例")
    @unittest.skipIf(False,"是否执行")
    def test01_Success(self):
        """正确登录"""
        loginPage = login.loginPage()
        loginPage.login("18502827849", "1234561")
        msg = loginPage.findElementByJQuery("li:contains('首页')")
        MainPage = Main.mainPage()
        MainPage.test()
        self.logEr.AssertIsNotNone(msg , "登录失败，未找到【首页】标题" , loginPage)

    @decorator.Call_CaseName("【用户名错误，密码正确】用例")
    @unittest.skipIf(True,"是否执行")
    def test02_NameError(self):
        """用户名错误，密码正确"""
        loginPage = login.loginPage()
        loginPage.login("18502827848", "123456")
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , "用户名或密码错误","用户名错误提示")
        loginPage.login("12345678901", "1234567")
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , "请输入正确的手机号码","非手机号数字提示")
        loginPage.login("asdf5678901", "1234567")
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , "请输入正确的手机号码","字符手机号提示")
        loginPage.login("1850282784", "123456")
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , "请输入正确的手机号码","手机号10位提示")
        loginPage.login("185028278499", "123456")
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , "请输入正确的手机号码","手机号12位提示")


    @decorator.Call_CaseName("【用户名正确，密码错误】用例")
    @unittest.skipIf(True,"是否执行")
    def test03_PdError(self):
        """用户名正确，密码错误"""
        loginPage = login.loginPage()
        loginPage.login("18502827849", "1234567")
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , "用户名或密码错误","密码错误提示")
        loginPage.login("18502827849", "12345")
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , "至少6个字符","至少6个字符")
        loginPage.login("18502827849", "1234567890123456789012345678901")
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , "最多30个字符","最多30个字符")

    @decorator.Call_CaseName("【用户名、密码错误】用例")
    @unittest.skipIf(False,"是否执行")
    def test04_NamePdError(self):
        """用户名、密码错误"""
        loginPage = login.loginPage()
        loginPage.login("18502827848", "1234567")
        error = loginPage.getTest("#login_error")
        MainPage = Main.mainPage()
        MainPage.test()
        self.logEr.AssertEqual(error, "用户名或密码错误", "用户、密码错误提示",loginPage)


if __name__=='__main__':
    #执行所有用例
    unittest.main()


