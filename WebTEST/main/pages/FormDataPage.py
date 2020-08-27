#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :LoginPage.py
# @Time      :2020/7/21 10:51
# @Author    :ZhouYue

from main.commom.base.BasicPage import BasicPage
import time
from main.data import static_variable

class FormDataPage(BasicPage):
    """
    添加表单数据页面
    """

    mainframe = "#iframeUseApp->#app-main-iframe"
    topframe = "#iframeUseApp"

    logger = BasicPage.logs.getlog(__name__)

    def TableList(self):
        self.switchToFrames(self.mainframe)

    def topFrame(self):
        self.switchToFrames(self.topframe)

    def intoApp(self,appName):
        """

        进入应用使用页面
        :param appName: 应用名称
        """
        self.switchMainFrame()
        self.click(self.findElementByJQuery("div[title='{0}']:visible".format(appName),10))

    def intoDataList(self,appName,formMenus):
        """
        根据应用及表单进入数据列表

        :param formMenus: 表单名称,多层菜单，用"->"隔开，如：菜单1->信息表
        :param appNmae： 应用名称
        """
        self.intoApp(appName)
        menus = formMenus.split("->")
        for i in range(len(menus)):
            self.topFrame()
            if (i == len(menus) - 1):
                selector = "i.menu-info:contains('{0}')".format(menus[i])
                isExist = self.findElementByJQuery(selector,2)
                assert (isExist != None),"没有该表单：{0}".format(menus[i])
                self.checkDataList(menus[i])

            else:
                selector = "p[class*=nav-tit]:contains('{0}')".format(menus[i])
                isExist = self.findElementByJQuery(selector,2)
                assert (isExist != None),"第{0}层没有该菜单：{1}".format(i,menus[i])
                open = "p[class*=open]:contains('{0}')".format(menus[i])
                isOpen = self.findElementByJQuery(open)
                if (isOpen == None):
                    self.clickByJs(selector)

    def checkDataList(self,formName):
        """

        点击表单菜单
        :param formName: 表单名称
        """
        self.clickByJs("i.menu-info:contains('{0}')".format(formName),5)

    def clickAdd(self,displayTitle):
        """

        数据列表中点击添加按钮，切换到添加窗口
        :param displayTitle： 新窗口标题部分文本
        """
        self.TableList()
        self.clickByJs("button:contains('添加')",5)
        self.switchToWindowByName(displayTitle)

if __name__ == "__main__":
    aa =123