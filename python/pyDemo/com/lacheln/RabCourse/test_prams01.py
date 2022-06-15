#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 4:53 下午
# @Author  : Lacheln
"""
参数化用例
"""

import pyDemo

# 单参数
search_list = ['appium']
@pyDemo.mark.parametrize('name', search_list)
def test_search_list(name):
    assert name in search_list

# 多参数
mal_paramer = [("1+2",3),("3+6",5),("2+2",0)]
mal_paramer_rename = ["number1","number2","number3"]
#ids=方法 实现测试用例重命名
@pyDemo.mark.parametrize("input,expect", mal_paramer, ids=mal_paramer_rename)
def test_mul_parameter(input,expect):
    #eval()方法可以将字符串进行转化，实现计算功能
    assert eval(input) == expect

#笛卡尔积
num1 = ["appnium","selinum","pyDemo"]
num2 = ["utf-8","gbk","gb2312"]
@pyDemo.mark.parametrize("wd", num1)
@pyDemo.mark.parametrize("code", num2)
def test_dkej(wd,code):
    print(f"wd:{wd},code:{code}")

test_dkej()