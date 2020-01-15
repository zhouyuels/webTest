#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :Browser.py
# @Time      :2019/12/3 17:26
# @Author    :ZhouYue
# @Description    :浏览器驱动设置，取的driver

import os
from selenium import webdriver
from main.config.readconfig import Readconfig
from main.commom.init.globalvar import globalvar

class Browser():
    """
    获取浏览器驱动
    """

    path = os.path.split(os.path.realpath(__file__))[0]
    setupPath = os.path.join(path, "../../config/SetUp.ini")
    browser = Readconfig(setupPath).get_value("BROWSER", "browser")
    if browser == "Ie":
        driver = webdriver.Ie(globalvar().DriverPath(browser))
    if browser == "Chrome":
        driver = webdriver.Chrome(globalvar().DriverPath(browser))

    # def __init__(self):
    #     path = os.path.split(os.path.realpath(__file__))[0]
    #     setupPath = os.path.join(path, "../../config/SetUp.ini")
    #     self.browser = Readconfig(setupPath).get_value("BROWSER","browser")

    def getDriver(self):
        """取得driver实例"""
        return Browser.driver

    def setDriver(self):
        """重新设置driver实例"""
        if Browser.browser == "Ie":
            driver = self.Ie()
        if Browser.browser == "Chrome":
            driver = self.Chrome()
        Browser.driver = driver


    def Ie(self):
        """启动Ie"""
        driver = webdriver.Ie(globalvar().DriverPath("Ie"))
        # driver.implicitly_wait(5)
        return driver

    def Chrome(self):
        """启动Chrome"""
        driver = webdriver.Chrome(globalvar().DriverPath("Chrome"))
        # driver.implicitly_wait(5)
        return driver


if __name__ == "__main__":
    aa =11

