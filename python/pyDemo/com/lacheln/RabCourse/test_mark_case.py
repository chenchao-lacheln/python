#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 5:32 下午
# @Author  : Lacheln

"""
标记测试用例
"""
#场景：app和web一套代码，需要实现分类
#解决：@pyDemo.mark.标签名
#执行：
#   pyDemo -vs test_xxx.py -m=标签名
#   pyDemo -vs test_xxx.py -m 标签名
#   pyDemo -vs test_xxx.py -m "not 标签名"

#Android
import pyDemo


@pyDemo.mark.android
def test_android():
    print("test android")
    assert 1 == 2
#ios
@pyDemo.mark.ios
def test_ios():
    print("test ios")
    assert 1 == 1
#web
@pyDemo.mark.web
def test_web():
    print("test weh")
    assert 2 == 2

"""
去掉  执行pytest -vs test_mark_case.py -m ios 命令后，出现的 1 warning in 0.01s  
创建pytest.ini文件
[pyDemo]
markers = ios
          android
          web
"""