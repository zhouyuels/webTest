#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test_run.py
# @Time      :2019/12/9 14:47
# @Author    :ZhouYue

import main.pages.loginPage as loginPage
import main.pages.input as input

loginPage = loginPage.login()
inputPage = input.input()


loginPage.openUrl("https://testpro.formtalk.net/login.do")
inputPage.browserMax()
name_str = "input[name=loginName]:visible"
pd_str = 'input[name=loginPassword]:visible'
ok_str = 'input#doLogin:visible'
name_el = inputPage.findElementByJQuery(name_str)
pd_el = inputPage.findElementByJQuery(pd_str)
ok_el = inputPage.findElementByJQuery(ok_str)


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



loginPage.type(name_str, "18502827849")
loginPage.typeByJs(pd_el, "123456")
inputPage.moveSlider("span.verifyCode-icon","span.labelTip")
inputPage.clickByJs(ok_el)


table = loginPage.findElementByJQuery("div[title='表单中心']:visible")
loginPage.click(table)

loginPage.switchToFrame(["#mainFrame"])
loginPage.click("span:contains('新的表单_测试')")
loginPage.click("button.form-udata-add-span")
loginPage.switchToWindowByName("云端应用自定义")


# time.sleep(1)
loginPage.close()
loginPage.quit()

