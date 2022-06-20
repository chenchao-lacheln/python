#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 15:28
# @Author  : Lacheln

# 第三方库：xlrd 、xlwings 、pandas

# openpyxl
#安装 ：pip install openpyxl
# 导入 import openpyxl

# data 存放Excel数据文件
# func 存放被测函数文件
# testcase 存放测试用例文件
import openpyxl

# 获取工作簿
book = openpyxl.load_workbook('params.xlsx')

# 获取工作表
sheet = book.active

# 获取单个单元格值
a_1 = sheet['A1'].value
print(a_1)
c_3 = sheet.cell(column=3,row=3).value
print(c_3)

# 获取多个单元格值
cells = sheet["A1" : "C3"]
print(type(cells),cells)