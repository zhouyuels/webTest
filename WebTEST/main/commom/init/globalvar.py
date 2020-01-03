#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :globalvar.py
# @Time      :2019/12/4 15:43
# @Author    :ZhouYue
# @Description    :设置全局变量

import os
from main.commom.tools.log import log

class globalvar():

    logs = log.Log()
    logger = logs.getlog()

    def DriverPath(self,browser = "Ie"):
        """设置浏览器,默认为IE浏览器

        :param
        type: 浏览器类型：Ie、Chrome
        """
        if browser == "Ie":
            DriverPath = self.IeDriver()
        elif browser == "Chrome":
            DriverPath = self.ChromeDriver()
        # driver = getattr(webdriver,browser.getBrowser())(DriverPath)
        return DriverPath

    def IeDriver(self):
        """设置浏览器为Ie浏览器"""
        dir_path = os.path.dirname(os.path.abspath(__file__))
        DriverPath = os.path.abspath(os.path.join(dir_path, "..\..\drivers\IEDriverServer.exe"))
        self.logger.debug(f'浏览器驱动为:{DriverPath}')
        return DriverPath

    def ChromeDriver(self):
        """设置浏览器为Chrome浏览器"""
        dir_path = os.path.dirname(os.path.abspath(__file__))
        DriverPath = os.path.abspath(os.path.join(dir_path, "..\drivers\chromedriver.exe"))
        self.logger.debug(f'浏览器驱动为:{DriverPath}')
        return DriverPath


if __name__ == "__main__":
    aa = 1






