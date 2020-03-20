#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :Excel_Operation.py
# @Time      :2020/1/18 11:21
# @Author    :ZhouYue
# @Description    : 操作excel文档

import xlrd, os, sys
from main.commom.tools.log import log
from xlutils.copy import copy

logs = log.Log()
logger = logs.getlog()

class OperationExcel():
    def __init__(self,file_name,sheet_name):
        #测试数据的路径
        self.xlsx_path = os.path.abspath(os.path.join(os.path.realpath(__file__), "../../../data/%s" % file_name))
        self.sheet_name = sheet_name
        logger.info("测试数据excle文档路径为：%s" % self.xlsx_path)

        #打开测试数据的excel文档的某个sheet
        self.data = xlrd.open_workbook(self.xlsx_path)
        self.table = self.data.sheet_by_name(self.sheet_name)

    def get_rows(self):
        """
        获取sheet的行数
        """
        return self.table.nrows

    def get_cell_data(self,rowx,colx):
        """
        获取单元格中的数据

        :param rowx: 行号
        :param colx: 列号
        :return: 返回单元格数据
        """
        return self.table.cell_value(rowx,colx)

    def get_row_data(self,row):
        """
        获取某一行的数据

        :param row: 行号
        :return: 返回行数据，列表类型
        """
        return self.table.row_values(row)

    def get_col_data(self,col):
        """
        获取某一列的数据

        :param col: 列号
        :return: 返回列数据，列表类型
        """
        return self.table.col_values(col)

    def get_row_num(self,case_id):
        """
        根据case_id获取行号

        :param case_id: case_id
        :return: 返回行号
        """
        row_num = 0
        row_nums = self.get_col_data(0)
        if case_id not in row_nums:
            logger.error("该case_id不在sheet中")
            return case_id
        else:
            for num in row_nums:
                if case_id == num:
                    return row_num
                row_num = row_num+1

    def get_caseid_data(self,case_id):
        """
        根据case_id获取数据

        :param case_id:
        :return: 返回行数据，列表类型
        """
        row_num = self.get_row_num(case_id)
        return self.table.row_values(row_num)

    def write_excel(self,sheet_name,row, col, value):
        """
        往excel中写入数据

        :param sheet_name: 工作单名称
        :param row: 行号
        :param col: 列号
        :param value: 要写入的数据
        :return:
        """
        rb = xlrd.open_workbook(self.xlsx_path, formatting_info=True)  # 参数说明: formatting_info=True 保留原excel格式
        sheetnames =rb.sheet_names()
        num = 0
        for name in sheetnames:
            if sheet_name == name:
                index = num
            num = num +1
        write_data = copy(rb)
        sheet_data = write_data.get_sheet(index)
        sheet_data.write(row, col, value)
        write_data.save(self.xlsx_path)

if __name__ == "__main__":
    file_name = "testdata.xlsx"
    sheet_name = "location_map"
    run = OperationExcel(file_name,sheet_name)
    a = run.get_cell_data(1,11)
    print(a)
    print(run.get_row_data(1))
    print(run.get_col_data(0))
    print(run.get_row_num(1))
    print(run.get_caseid_data(1))
    run.write_excel(sheet_name,1,10,"aaa")