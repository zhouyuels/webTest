#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :JQmodel.py
# @Time      :2020/1/2 17:03
# @Author    :ZhouYue
# @Description    :

from main.commom.init.Browser import Browser

class JQModel():


    def injectJQueryIfNeeded(self):
        """

        往页面注入JQuery
        """
        if self.isJQueryLoaded() == False:
            self.injectjQuery()

    def isJQueryLoaded(self):
        """
        验证页面是否已加载JQuery

        :return:True/False
        """
        try:
            from main.pages.BasicPage import BasicPage
            hasJQuery = Browser().driver.execute_script("return typeof jQuery == 'function';")
            if hasJQuery == False:
                print("页面未注入JQuery")
        except Exception as e:
            hasJQuery = False
            print("页面未注入JQuery")
        return hasJQuery

    def injectjQuery(self):
        """

        注入JQuery
        """
        Browser().driver.execute_script('var bod = document.getElementsByTagName("body")[0];'
                                'var script = document.createElement("script");'
                                'script.setAttribute("src","https://code.jquery.com/jquery-1.9.1.js");'
                                'script.setAttribute("type","text/JavaScript");'
                                'bod.appendChild(script)')
        print("往页面未注入JQuery")



if __name__ == "__main__":
    run_code = 0