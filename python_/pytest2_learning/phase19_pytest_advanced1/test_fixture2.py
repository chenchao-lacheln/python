#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 01:03
# @Author  : Lacheln

""" fixture的作用域"""
import pytest

# 定义登录的fixture,尽量避免以test_开头(相当于一个公共方法，避免与测试case混淆)
# @pytest.fixture() # # fixture底层源码，默认是function级别 函数级别
# @pytest.fixture(scope="module") #模块级别
@pytest.fixture(scope="class") #类级别
def login():
    print("完成登录操作")

def test_search():
    print("搜索")

def test_cart(login):
    # login()
    print("购物车")

def test_order(login):
    # login()
    print("订单")

class TestDemo1():

    def test_case1(self,login):
        print("case1")

    def test_case2(self,login):
        print("case2")
