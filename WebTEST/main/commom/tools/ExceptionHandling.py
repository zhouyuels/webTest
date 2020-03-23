#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :ExceptionHandling
# @Time      :2020/03/23 17:10
# @Author    :ZhouYue
# @Description    : 
#--------------------------------------------------------

import traceback
import unittest

class ExceptionHandling(unittest.TestCase):

    def logExceptinMsg(self,exception,Page):
        """
        打印AssertionError的错误日志
        :Args:
         - exception: 捕获的错误信息。如：Exception as e，中的e
         - Page: 需要打印日志的页面
        """
        er = traceback.format_exc()
        Page.logger.error(exception)
        Page.logger.error(er)

    def AssertEqual(self,first,second,er_msg,Page):
        """
        判断两个值是否相等
        :Args:
         - first: 第一个值
         - second: 第二个值
         - er_msg: 错误信息，若不想打，则输出该错误信息日志
         - Page: 需要打印日志的页面
        """
        try:
            self.assertEqual(first , second,er_msg)
        except Exception as e:
            self.logExceptinMsg(e, Page)
            self.assertEqual(first, second, er_msg)

    def AssertIsNotNone(self,first,er_msg,Page):
        """
        判断值是否不为空
        :Args:
         - first: 要判断的值
         - er_msg: 错误信息，若不想打，则输出该错误信息日志
         - Page: 需要打印日志的页面
        """
        try:
            self.assertIsNotNone(first,er_msg)
        except Exception as e:
            self.logExceptinMsg(e, Page)
            self.assertIsNotNone(first,er_msg)