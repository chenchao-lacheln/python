#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 01:33
# @Author  : Lacheln


"""=================常用的异常处理方式================="""

# try except

try:
    a = int(input("輸入被除数: "))
    b = int (input("輸入除数: "))
    c=a/b
    print("悠輸入的兩个数相除的結果是: ", c )
except (ValueError, ArithmeticError) :
    print("程序岌生了数字格式昇常、算ポ昇常之一" )
except:
    print("未知昇常")
    print ("程序継姨返行")


# pyDemo.raises()

# 可以捕获特定的异常
# 获取捕获的异常的细节(异常类型，异常信息)
# 发生异常，后面的代码将不会被执行
