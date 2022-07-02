#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 01:46
# @Author  : Lacheln

import pytest


"""不需要导入，直接引用conftest.py方法"""

def test_search(login):
    print("搜索")

def test_cart(login):
    # login()
    print("购物车")

def test_order(login):
    # login()
    print("订单")