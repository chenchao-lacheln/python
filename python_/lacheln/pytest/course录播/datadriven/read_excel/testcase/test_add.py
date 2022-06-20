#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 16:41
# @Author  : Lacheln

# testcase 存放测试用例文件
import openpyxl
import pytest



def get_excel():
#     获取工作薄
    book = openpyxl.load_workbook('../data/params.xlsx')
#     获取工作表
    sheet = book.active
#   返回数据结构 [[1,2,3],[3,6,9],[100,200,300]]
    values = []
    for row in sheet:
        line = []
        for cell in row:
            line.append(cell.value)
        values.append(line)
    print(values)
    return values

class TestWithEXECL:
    @pytest.mark.parametrize('x,y,expected',get_excel())
    def test_add(self,x,y,expected):
        assert x,y == expected

