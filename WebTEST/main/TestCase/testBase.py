#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :testBase.py
# @Time      :2020/1/11 14:59
# @Author    :ZhouYue
# @Description    :测试用例基础设置，每个测试用例均继承该类

import unittest,json,time, traceback
from common.keywords import decorator
from main.pages.BasicPage import BasicPage


class testBase(unittest.TestCase):
    """
    测试用例基础设置
    """

    test_name

    @classmethod
    def setUpClass(cls):
        """终端鉴权上线"""
        cls.logger.info(u"【***********START TEST:%s***********】")
        case_id = 0
        """从用例文档中取参数和拼接参数"""
        data = json.loads(cls.open_sheet.get_cell_data(cls.open_sheet.get_row_num(case_id), excel_config.get_params()))
        header = json.loads(cls.open_sheet.get_cell_data(cls.open_sheet.get_row_num(case_id), excel_config.get_headers()))
        token_key = str(cls.open_sheet.get_cell_data(cls.open_sheet.get_row_num(case_id), excel_config.get_token()))
        if token_key == "yes":
            token = get_token.token().gettoken()
            header["token"] = token
        else:
            pass
        """调接口使设备鉴权上线"""
        run = httpRequest.httprequest(cls.tool_ip,cls.tool_path)
        run.Request_POST(data=data,headers=header,timeout=3)
        cls.logger.info(u"设备鉴权并已上线")

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        Revolve.logger.info(u"【***********END TEST:Revolve***********】")

    @decorator.Call_CaseName(u"【逻辑通道号验证】case_id:1")
    @unittest.skipIf(do_something_for_test.do_something().is_run(filename, sheet, 1), u"用例文档中是否执行")
    def test_01_logicChannelNo_true(self):
        """逻辑通道号验证,case_id:1"""
        case_id = 1
        """从用例文档中取参数和拼接参数"""
        data = json.loads(self.open_sheet.get_cell_data(self.open_sheet.get_row_num(case_id), excel_config.get_params()))
        header = json.loads(self.open_sheet.get_cell_data(self.open_sheet.get_row_num(case_id), excel_config.get_headers()))
        token_key = str(self.open_sheet.get_cell_data(self.open_sheet.get_row_num(case_id), excel_config.get_token()))
        variable = json.loads(self.open_sheet.get_cell_data(self.open_sheet.get_row_num(case_id), excel_config.get_variable()))
        excpet_rse = json.loads(
            self.open_sheet.get_cell_data(self.open_sheet.get_row_num(case_id), excel_config.get_except_res()))
        if token_key == "yes":
            token = get_token.token().gettoken()
            header["token"] = token
        else:
            pass
        error_num = []
        for logicChannelNo_num in variable:

            """获取验签"""
            data["logicChannelNo"] = logicChannelNo_num
            sign = create_new_sign.create_sign(static_variable.appKey, static_variable.secretKey).postSign(data)
            data["appKey"] = static_variable.appKey
            data["sign"] = sign["sign"]
            data["timestamp"] = sign["timestamp"]
            """调接口及获取断言数据"""
            run = httpRequest.httprequest(self.ip,self.path)
            res = run.Request_POST(data=data, headers=header, timeout=3)
            """断言验证"""
            try:
                self.assertEqual(res.status_code, 200)
                self.assertEqual(res.json()["returnSuccess"], excpet_rse["returnSuccess"])
                self.assertEqual(res.json()["returnErrCode"], excpet_rse["returnErrCode"])
                self.assertEqual(res.json()["returnErrMsg"], excpet_rse["returnErrMsg"])
            except Exception as e:
                er = traceback.format_exc()
                self.logger.error(e)
                self.logger.error(er)
                error_num.append(logicChannelNo_num)
                res_error = res.text
                continue
        """把实际返回的response和用例通过结果写入excel用例文档"""
        if len(error_num) == 0:
            result = excel_config.get_succesed()
            self.open_sheet.write_excel(self.sheet, self.open_sheet.get_row_num(case_id), excel_config.get_result(), result)
            self.open_sheet.write_excel(self.sheet, self.open_sheet.get_row_num(case_id), excel_config.get_response(), res.text)
        else:
            result = excel_config.get_failed()
            self.open_sheet.write_excel(self.sheet, self.open_sheet.get_row_num(case_id), excel_config.get_result(), result)
            self.open_sheet.write_excel(self.sheet, self.open_sheet.get_row_num(case_id), excel_config.get_response(), res_error)
            self.logger.error(u"逻辑通道号：%r错误" % error_num)
        self.assertEqual(result, excel_config.get_succesed())


if __name__=='__main__':
    #执行所有用例
    unittest.main()


