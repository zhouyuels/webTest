#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :run.py
# @Time      :2020/1/18 15:53
# @Author    :ZhouYue
# @Description    : 运行控制文件

import time,os
from HTMLTestRunner import HTMLTestRunner
import unittest
from main.commom.tools.log import logs_setup

class Run():

    def __init__(self,file_path,logs_name,rp_name):
        """
        初始化日志配置文件，及测试报告配置

        :param file_path: 存放日志文件和测试报告的路径
        :param logs_name: 日志文件名称
        :param rp_name: 测试报告名称
        """

        """文件保存路径，如果不存在就会被重建"""
        self.now = time.strftime("%Y-%m-%d_%H-%M-%S")
        file_path = "%s_%s" % (file_path,self.now)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        """初始化日志配置（日志文件存放路径、日志文件名称，绝对路径）"""
        logs_name = "%s_%s" %(logs_name,self.now)
        set_log = logs_setup.Logs_setup()
        set_log.set_logsName(file_path,logs_name)
        """初始化测试报告配置（测试报告存放路径、报告信息，绝对路径）"""
        # 测试用例目录
        self.test_dir = '../TestCase'
        #定义报告路径、名称
        #self.file_path = "../Result/Test_report_%s.html" % self.now
        self.path = "%s/%s_%s.html" % (file_path,rp_name,self.now)

    def run_all(self,reporter_title,reporter_description):
        """
        unittest框架的defaultTestLoader()类，

        通过该类下面的discover()方法可自动根据测试目录test_dir匹配查找测试用例文件（test*.py），
        并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover
        :return:
        """
        from main.commom.tools.log import log
        logs = log.Log()
        logger = logs.getlog()
        #匹配测试用例后加载用例
        discover = unittest.defaultTestLoader.discover(self.test_dir, pattern='test*.py')
        if discover.countTestCases() > 0:
            #执行测试用例并生成报告
            fp = open(self.path, 'wb')
            runner = HTMLTestRunner(stream=fp, title=reporter_title, description=reporter_description)
            runner.run(discover)
            fp.close()
        else:
            logger.info(u"没有可执行的测试用例，或未找到匹配的测试文件")

        #执行测试用例不生成报告
        #runner = unittest.TextTestRunner(verbosity=2)
        #runner.run(discover)

if __name__ == "__main__":
    """日志配置参数"""
    log_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../result/reporter_logs"))
    log_name = "Test-Logs"
    rp_name = "Test_report"
    """报告配置参数"""
    reporter_title = "调试_测试报告"
    reporter_description = "代码调试"

    """运行主函数"""
    run = Run(log_path, log_name, rp_name)
    case_run = run.run_all(reporter_title,reporter_description)


