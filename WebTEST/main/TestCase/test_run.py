#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test_run.py
# @Time      :2019/12/9 14:47
# @Author    :ZhouYue

import main.pages.LoginPage as loginPage
import main.pages.MainPage as input
import time

loginPage = loginPage.loginPage()
inputPage = input.mainPage()


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

loginPage.loginUrl("https://testpro.formtalk.net/login.do")
"""登录"""
loginPage.login("18502827849","123456")

loginPage.click("div[title='表单中心']")
loginPage.switchToFrame(["#mainFrame"])
loginPage.click("span:contains('新的表单_测试')")
loginPage.click("button.form-udata-add-span")
loginPage.switchToWindowByName("新的表单_测试")

loginPage.type("label:contains(单行文本)+div>input","姓名")
# loginPage.selectByIndex("select",1)
# loginPage.selectByValue("select","2")
loginPage.selectByText("select","选项1")
time.sleep(1)
loginPage.close()
loginPage.quit()

