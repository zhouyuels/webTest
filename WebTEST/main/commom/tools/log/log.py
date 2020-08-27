#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :log.py
# @Time      :2020/1/3 15:46
# @Author    :ZhouYue
# @Description    :

import logging,logging.config
import sys,os
import threading

lock = threading.Lock()

class Log():

    """
    初始化日志设置，通过读取日志配置文件初始化日志
    """
    """读取日志配置文件内容"""
    path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../../config/configFile/Log.ini"))
    logging.config.fileConfig(path)

    def getlog(self,logger_name = "Logs"):
        lock.acquire()
        logger = logging.getLogger(logger_name)
        lock.release()
        return logger

if __name__ == "__main__":
    run = Log()
    logger = run.getlog("fdfasf")
    # 日志输出l
    logger.debug('debug message')
    logger.info('info message')

    run1 = Log()
    logger1 = run1.getlog("ppppppp")
    logger1.warning('warn message')
    logger1.error('error message')
    logger1.critical('critical message')





