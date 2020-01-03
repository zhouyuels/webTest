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
    def __init__(self):
        """
        初始化日志设置，通过读取日志配置文件初始化日志
        """
        """读取日志配置文件内容"""
        self.path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../../config/Log.ini"))
        logging.config.fileConfig(self.path)
        """创建一个日志器logger"""
        self.logger = logging.getLogger('Logs')

    def getlog(self):
        lock.acquire()
        logger = self.logger
        lock.release()
        return logger
if __name__ == "__main__":
    run = Log()
    logger = run.getlog()
    # 日志输出l
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')



if __name__ == "__main__":
    run_code = 0