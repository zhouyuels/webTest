#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :Readconfig.py
# @Time      :2019/12/5 16:31
# @Author    :ZhouYue
# @Description    :操作配置ini文件

from configparser import ConfigParser
import os,sys

class Readconfig():
    """
    操作配置ini文件
    """

    def __init__(self,path):

        self.cf = ConfigParser()
        self.cf.read(path)

    def get_sections(self):
        """
        获取配置文件的所有域
        """
        sections = self.cf.sections()
        return sections

    def get_options(self,sections_name):
        """
        获取配置文件某个域下的所有key
        """
        options = self.cf.options(sections_name)
        return options

    def get_value(self,sections_name,key):
        """
        获取配置文件某个配置的值
        """
        #取配置值
        value = self.cf.get(sections_name, key)
        return value


if __name__ == "__main__":
    # PATH指一个文件的全路径作为参数：C
    # 如果给出的是一个目录和文件名，则输出路径和文件名
    # 如果给出的是一个目录名，则输出路径和为空文件名
    path = os.path.split(os.path.realpath(__file__))[0]
    setup_path = os.path.join(path, "SetUp.ini")  # 配置文件路径
    print(setup_path)
    run = Readconfig(setup_path)
    aa = run.get_value("BROWSER","browser")