#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :logs_setup.py
# @Time      :2020/1/3 15:47
# @Author    :ZhouYue
# @Description    :


import time,os,sys
from configparser import ConfigParser
from main.commom.tools.log import log

class Logs_setup():
    """
    初始化配置日志路径及名称
    """
    def __init__(self):
        """获取日志配置文件路径"""
        self.path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../../config/configFile/Log.ini"))
        print(self.path)

    def set_logsName(self,log_path,logs_name):
        """设置日日志初始化信息

        :param log_path: 设置日志文件路径
        :param logs_name: 设置日志文件名称
        :return:
        """
        config = ConfigParser()
        config.read(self.path)
        """修改日志文件名"""
        set_args = '(r"%s\%s.log" , "a")' % (log_path,logs_name)
        config.set("handler_file", "args", set_args)
        with open(self.path, "w+") as f:
            config.write(f)
        logs = log.Log()
        logs.logger.info(u"日志文件路径问：%s" % log_path)
        logs.logger.info(u"日志文件名称为：%s" % logs_name)

if __name__ == '__main__':

    logs_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../../result"))
    logs_name = "Test-Logs"
    run =  Logs_setup()
    run.set_logsName(logs_path,logs_name)