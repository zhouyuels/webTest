#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test001_login.py
# @Time      :2020/7/21 10:36
# @Author    :ZhouYue
# @Description    :

import unittest,json
import main.commom.base.testBase as testBase
import main.pages.LoginPage as login
import main.pages.FormDataPage as FormData
from main.commom.tools import decorator
from main.data import static_variable
from main.commom.tools import Excel_Operation


class Login(testBase.testBase):
    """表单数据列表添加数据"""

    filename = static_variable.case_file
    sheet = "添加数据"
    open_sheet = Excel_Operation.OperationExcel(filename, sheet)


    @decorator.Call_CaseName("【添加数据】用例")
    @unittest.skipIf(False,"是否执行")
    def test01_Success(self):

        """获取用例数据"""
        loginPage = login.loginPage()
        FormDataPage = FormData.FormDataPage()
        case_row = self.open_sheet.get_row_num(1)
        """进入登录页面，登录"""
        loginMsg = json.loads(self.open_sheet.get_cell_data(case_row+1,4))
        loginPage.login(loginMsg["user"], loginMsg["pd"])
        """进入表单数据列表"""
        formMsg = json.loads(self.open_sheet.get_cell_data(case_row+2,4))
        FormDataPage.intoDataList(formMsg["应用名称"],formMsg["表单菜单"])
        FormDataPage.clickAdd(formMsg["表单菜单"])
        """填写表单数据"""
        dataMsg = json.loads(self.open_sheet.get_cell_data(case_row + 4, 4))
        FormDataPage.logger.debug(dataMsg)
        FormDataPage.type("label:contains(单行文本)+div>input[type=text]",dataMsg["单行文本"])
        FormDataPage.clickByJs("button:contains('保存')")

if __name__=='__main__':
    #执行所有用例
    unittest.main()


