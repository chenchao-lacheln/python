#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 3:00 下午
# @Author  : Lacheln
"""
测试框架结构
"""

# 模块级(setup_ module/teardown_ module)模块始末，全局的(优先最高)
# 函数级(setup_ function/teardown_ function) 只对函数用例生效(不在类中)
# 类级(setup_ class/teardown_ class)只在类中前后运行一 次(在类中)
# 方法级(setup_ method/teardown_ methond)开始于方法始末 (在类中)
# 类里面的(setup/teardown) 运行在调用方法的前后

# 模快級別 只被调用一次
def setup_module():
    print("资源准备: setup module")

def teardown_module():
    print("资源销毁: teardown module")


def test_case1():
    print("case1")


def test_case2():
    print("case2")

def setup_function():
    print("资源准备: setup function")

def teardown_function():
    print("资源销毁: teardown function")


class TestDemo:
# 执行类前后分别执行setup_ .class teardown_class
    def setup_class(self):
        print("TestDemo setup_ class")
    def teardown_class(self):
        print ("TestDemo teardown_ class")
    #每个类里面的方法前后分别执行setup, teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")

    def test_demo3(self):
        print("test demo3")