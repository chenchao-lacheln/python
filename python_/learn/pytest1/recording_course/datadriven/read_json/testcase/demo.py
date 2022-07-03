#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 23:46
# @Author  : Lacheln

'''
●查看json文件
    pycharm
    txt记事本
●读取json文件
    内置函数open()--负责连接文件和读取文件的内容
    内置库json--提供一系列解析json数据的方法
        方法: json.loads()  # 解析json文本对象或者文件并且返回一个字典对象
        方法: json.dumps()  # 与json.loads( )相反，接收一个字典对象，并将改字典转换成文本形式的json对象
'''
import json

# 定义获取json文件的函数

def get_json():
    with open('../data/demo.json', 'r') as file:
        data = json.loads(file.read())
        print(type(data),data)
        s = json.dumps(data,ensure_ascii=False)   #ensure_ascii 解析中文字符
        print(s,type(s))
if __name__ == '__main__':
    get_json()
