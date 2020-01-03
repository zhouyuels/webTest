#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test1.py
# @Time      :2020/1/2 9:53
# @Author    :ZhouYue
# @Description    :

from main.commom.tools.log import log

run = log.Log()
logger = run.getlog()
# 日志输出l
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
