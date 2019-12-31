#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :decorator.py.py
# @Time      :2019/12/11 15:53
# @Author    :ZhouYue

from selenium import webdriver
import os,time

webdriver.IeOptions()
dir_path = os.path.dirname(os.path.abspath(__file__))
DriverPath = os.path.abspath(os.path.join(dir_path, "..\..\drivers\IEDriverServer.exe"))
driver = webdriver.Ie(DriverPath)
driver.get("https://testpro.formtalk.net/login.do")
driver.find_element_by_css_selector("input[name=loginName]").send_keys("18502827849")
driver.find_element_by_css_selector('input[name=loginPassword]').send_keys("123456")
action = webdriver.ActionChains(driver)
SliderVerifyCodeIcon = driver.find_element_by_css_selector("span.verifyCode-icon")
Size = driver.find_element_by_css_selector("span.labelTip").size
action.drag_and_drop_by_offset(SliderVerifyCodeIcon, Size["width"], 0).perform()
action.release().perform()
action.move_to_element(SliderVerifyCodeIcon).release()
driver.find_element_by_css_selector('input#doLogin').click()

time.sleep(2)
driver.find_element_by_css_selector("div[title='表单中心']").click()
mainFrame = driver.find_element_by_css_selector("#mainFrame")
driver.switch_to.frame(mainFrame)
time.sleep(2)
driver.find_element_by_css_selector("body > div > div > div > div > div.form-info-list > ul > li:nth-child(2) > div > span").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.ours-common-area > div > section > section > div > div.ours-toolbar-area.ours-btns-area > button.form-udata-add-span.btns-info").click()

time.sleep(5)
driver.close()
driver.quit()





