#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 15:28
# @Author  : Lacheln

# 第三方库：xlrd 、xlwings 、pandas

# openpyxl
#安装 ：pip install openpyxl
# 导入 import openpyxl

import openpyxl

# 获取工作簿
book = openpyxl.load_workbook('params.xlsx')

# 获取工作表
sheet = book.active

# 获取单元格
a_1 = sheet['A1'].value
print(a_1)