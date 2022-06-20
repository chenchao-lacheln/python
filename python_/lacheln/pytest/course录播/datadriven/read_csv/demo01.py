#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 17:17
# @Author  : Lacheln

'''
●csv: 逗号分隔值
●是Comma-Separated Values的缩写
●以纯文本形式存储数字和文本
●文件由任意数目的记录组成
●每行记录由多个字段组成
'''
import csv


def get_csv():
    with open('data/demo.csv', 'r') as file:
        raw = csv.reader(file)

        for line in raw:
            print(line)

if __name__ == '__main__':
    get_csv()