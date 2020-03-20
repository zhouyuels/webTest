#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :MainPage.py
# @Time      :2019/12/5 18:07
# @Author    :ZhouYue


from main.commom.base.BasicPage import BasicPage

class mainPage(BasicPage):

    logger = BasicPage.logs.getlog(__name__)

    def test(self):
        self.logger.debug("Log_Test")

if __name__ == "__main__":
    aa =123