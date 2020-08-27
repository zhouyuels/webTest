#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test_run.py
# @Time      :2019/12/9 14:47
# @Author    :ZhouYue

from main.commom.init.Browser import Browser
import main.pages.LoginPage as login
import main.pages.MainPage as input
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


def test1():
    driver = webdriver.Chrome(r"F:\automation_git\FormTalk\WebTEST\main\drivers\chromedriver.exe")
    driver.get("https://testpro.formtalk.net/login.do")
    driver.maximize_window()
    driver.find_element_by_css_selector("input[name=loginName]").send_keys("17111111111")
    time.sleep(1)
    driver.find_element_by_css_selector('input[name=loginPassword]').send_keys("123456")
    time.sleep(1)
    action = ActionChains(driver)
    SliderVerifyCodeIcon = driver.find_element_by_css_selector("span.verifyCode-icon")
    action.drag_and_drop_by_offset(SliderVerifyCodeIcon, driver.find_element_by_css_selector(("span.labelTip")).size["width"], 0).perform()
    action.release().perform()
    action.move_to_element(SliderVerifyCodeIcon).release()

    """登录"""
    time.sleep(1)
    driver.find_element_by_css_selector('input#doLogin').click()
    time.sleep(10)
    driver.switch_to.default_content()
    driver.find_element_by_css_selector("div[title=自动化应用准备1_新版]").click()
    time.sleep(2)
    driver.switch_to.frame(driver.find_element_by_css_selector("#iframeUseApp"))
    driver.switch_to.frame(driver.find_element_by_css_selector("#app-main-iframe"))
    driver.find_element_by_css_selector("button.form-udata-add-span.btns-info").click()
    driver.switch_to.window(driver.window_handles[-1])
    driver.switch_to.window(driver.window_handles[0])
    print("切换成功")


    time.sleep(15)
    # loginPage.close()
    # loginPage.quit()

# test1()
# test2()
print("div[title='{0}']:visible".format("aaa"))