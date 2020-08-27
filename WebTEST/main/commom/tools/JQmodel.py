#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :JQmodel.py
# @Time      :2020/1/2 17:03
# @Author    :ZhouYue
# @Description    :

from main.commom.init.Browser import Browser
import time
from main.commom.tools.log import log

class JQModel():

    logs = log.Log()
    logger = logs.getlog(__name__)

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
            hasJQuery = Browser().driver.execute_script("return typeof jQuery == 'function';")
            if hasJQuery == False:
                self.logger.debug("页面未注入JQuery")
        except Exception as e:
            hasJQuery = False
            self.logger.debug("页面未注入JQuery")
        # print("JQuery:"+str(hasJQuery))
        return hasJQuery

    def injectjQuery(self):
        """

        注入JQuery
        """
        Browser().driver.execute_script('var bod = document.getElementsByTagName("body")[0];'
                                'var script = document.createElement("script");'
                                # 'script.setAttribute("src","http://code.jquery.com/jquery-1.9.1.js");'
                                'script.setAttribute("src","https://libs.baidu.com/jquery/1.9.1/jquery.min.js");'
                                'script.setAttribute("type","text/JavaScript");'
                                'bod.appendChild(script)')
        self.logger.debug("往页面注入JQuery")
        start = time.time()
        start_milli_time = int(time.time()*1000)
        timeout = 20*1000
        while int(time.time()*1000) - start_milli_time <= timeout:
            time.sleep(float(0.5))
            if (self.isJQueryLoaded() == True):
                break
        if (self.isJQueryLoaded()):
            self.logger.debug("页面注入JQuery成功,JQuery:"+str(self.isJQueryLoaded()))
        else:
            self.logger.debug("页面注入JQuery失败")
        self.logger.debug("耗时：%sS" % (time.time() - start))




if __name__ == "__main__":
    run_code = JQModel()
