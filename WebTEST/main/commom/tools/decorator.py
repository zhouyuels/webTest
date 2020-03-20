#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :decorator.py.py
# @Time      :2019/12/11 15:53
# @Author    :ZhouYue


from functools import wraps

def Call_CaseName(name):
    """
    打印执行的用例的名称

    :param name: 用例名称
    """
    def CaseName(func):
        @wraps(func)
        def call_name(self,*args, **kwargs):
            self.logger.info (u"执行case:%s" % name)
            return func(self,*args, **kwargs)
        return call_name
    return CaseName

#--------------------------------------------

def get_exception(METHOD):
    """
    接口调用异常处理

    :param METHOD: 接口方法，大写
    """
    def run_http(func):
        @wraps(func)
        def exception(self,*args, **kwargs):
            """
            #取调接口的参数
            keys = kwargs.keys()
            data = {}
            for n in keys:
                data[n] = kwargs[n]
            """
            """打印接口信息"""
            self.logger.info(u"Call Interface----------------\nURL：%s\nMETHOD：%s\nPARAMS：%s"
                             #u"接口参数：TestData：%s，json_data：%s，params：%s"
                             % (self.ip+self.path,METHOD,kwargs))
            try:
                res = func(self,*args, **kwargs)
                #result = res.json()
                #print json.dumps(result, ensure_ascii=False)
                if res.status_code == 200:
                    self.logger.info(u"请求地址：%s，status_code：%s，响应时间：%ss，返回结果：%s"
                                     % (res.url,res.status_code,res.elapsed.total_seconds(),res.text))
                    self.logger.info(u"-------------------Call Interface end----------------")

                else:
                    self.logger.error(u"响应错误：%s，status_code：%s，返回结果：%s"
                                      % (res.url,res.status_code,res.text))
                    self.logger.info(u"-------------------Call Interface end----------------")
                res.close()
                return res
            except Exception as e:
                self.logger.error(u"请求失败:%s"
                                  "\n-------------------------------The End----------------------------------"
                                  % e)
                return e
        return exception
    return run_http







