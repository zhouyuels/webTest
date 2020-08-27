#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test001_login.py
# @Time      :2020/1/11 14:56
# @Author    :ZhouYue
# @Description    :

import unittest,json
import main.commom.base.testBase as testBase
import main.pages.LoginPage as login
import main.pages.MainPage as Main
from main.commom.tools import decorator
from main.data import static_variable
from main.commom.tools import Excel_Operation


class Login(testBase.testBase):
    """登录测试"""

    filename = static_variable.case_file
    sheet = "web自动化"
    open_sheet = Excel_Operation.OperationExcel(filename, sheet)


    @decorator.Call_CaseName("【正确登录】用例")
    @unittest.skipIf(False,"是否执行")
    def test01_Success(self):
        """正确登录"""

        loginPage = login.loginPage()
        case_row = self.open_sheet.get_row_num(1)
        """进入登录页面，登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+1,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        """进入首页，显示首页的信息"""
        msg = loginPage.findElementByJQuery(f"li:contains('{self.open_sheet.get_cell_data(case_row+2,4)}')")
        self.assertIsNotNone(msg,"登录失败，未找到【首页】标题")

    @decorator.Call_CaseName("【用户名错误，密码正确】用例")
    @unittest.skipIf(False,"是否执行")
    def test02_NameError(self):
        """用户名错误，密码正确"""

        loginPage = login.loginPage()
        case_row = self.open_sheet.get_row_num(2)
        """进入登录页面，登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+1,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+2,4))
        """登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+3,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+4,4))
        """登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+5,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+6,4))
        """登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+7,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+8,4))
        """登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+9,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+10,4))

    @decorator.Call_CaseName("【用户名正确，密码错误】用例")
    @unittest.skipIf(False,"是否执行")
    def test03_PdError(self):
        """用户名正确，密码错误"""

        loginPage = login.loginPage()
        case_row = self.open_sheet.get_row_num(3)
        """进入登录页面，登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+1,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+2,4))
        """登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+3,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+4,4))
        """登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+5,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+6,4))

    @decorator.Call_CaseName("【用户名、密码错误】用例")
    @unittest.skipIf(False,"是否执行")
    def test04_NamePdError(self):
        """用户名、密码错误"""

        loginPage = login.loginPage()
        case_row = self.open_sheet.get_row_num(4)
        """进入登录页面，登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+1,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        error = loginPage.getTest("#login_error")
        self.assertEqual(error , self.open_sheet.get_cell_data(case_row+2,4))


if __name__=='__main__':
    #执行所有用例
    unittest.main()


