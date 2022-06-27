#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 01:57
# @Author  : Lacheln


"""在conftest.py中设置 @pytest.fixture(scope="function",autouse=True) """

def test_search():
    print("搜索")

def test_cart():
    # login()
    print("购物车")

def test_order():
    # login()
    print("订单")