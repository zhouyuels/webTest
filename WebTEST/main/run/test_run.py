#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test_run.py
# @Time      :2019/12/9 14:47
# @Author    :ZhouYue

from main.commom.init.Browser import Browser
import main.pages.LoginPage as login
import main.pages.MainPage as Main
# import main.pages.MainPage as input
import time
from selenium import webdriver
from main.commom.tools.log import log

def test1():
    Browser().setDriver()
    print(Browser().driver)
    loginPage = login.loginPage()

    # print("窗口标题为：",loginPage.getTitle())
    # print("页面url为：",loginPage.getUrl())
    # print("按钮坐标为：",loginPage.Location(ok_str))
    # print("按钮大小为：",loginPage.Size(ok_str))
    # print("按钮是否可见：",loginPage.isDisplayed(ok_str))
    # print("按钮是否选中：",loginPage.isSelected(ok_str))
    # print("按钮文本为：",loginPage.getTest("span.labelTip"))
    # print("按钮value属性值为：",loginPage.getAttribute(ok_str,"value"))
    # loginPage.setAttribute(name_str,"style","background: red; border: 2px solid red")
    # print("按钮value属性值为：",loginPage.getAttribute(name_str,"style"))

    """登录"""
    # loginPage.loginUrl("https://pro.formtalk.net/login.do")
    loginPage.login("17111111111","123456")
    # loginPage.click("div[title='自动化应用准备1_新版']")
    # loginPage.switchToFrame(["#iframeUseApp"])
    # loginPage.click("i.menu-info:contains('表单准备1')")
    # loginPage.switchToFrame(["#iframeUseApp","#app-main-iframe"])
    # loginPage.click("button:contains('添加')")
    # loginPage.switchToWindowByName("表单准备1")
    # loginPage.type("label:contains('单行文本')+div>input[type=text]","测试一下")

    # loginPage.click("div[title='表单中心']")
    # loginPage.switchToFrame(["#mainFrame"])
    # loginPage.click("span:contains('新的表单_测试')")
    # loginPage.click("button.form-udata-add-span")
    # loginPage.switchToWindowByName("新的表单_测试")

    # loginPage.type("label:contains(单行文本)+div>input","姓名")
    # loginPage.selectByIndex("select",1)
    # loginPage.selectByValue("select","2")
    # loginPage.selectByText("select","选项1")

    # loginPage.move(loginPage.findElementByJQuery("div[title='社会化招聘2.0']"))
    # loginPage.move("i[title='简历获取']")
    # loginPage.move("i[title='投递简历']")
    # loginPage.click("i[title='投递简历']")
    # time.sleep(5)

    loginPage.close()
    loginPage.quit()

def test2():
    Browser().setDriver()
    print(Browser().driver)
    loginPage = login.loginPage()
    """登录"""
    loginPage.login("18502827849","123456")
    loginPage.close()
    loginPage.quit()

test1()
test2()
