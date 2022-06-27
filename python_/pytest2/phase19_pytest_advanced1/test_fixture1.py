#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 00:52
# @Author  : Lacheln

import pytest

"""定义fixture————模拟setup"""

# 定义登录的fixture
@pytest.fixture()
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
