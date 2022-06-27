#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 01:18
# @Author  : Lacheln

"""yield关键字————模拟teardown"""

import pytest

# 定义登录的fixture
@pytest.fixture()
def login():
    # setup操作
    print("完成登录操作")
    token  = "adsadadsdasfas"
    username = "jhkjfdjskf"
    yield token,username# 相当于return 没有添加东西 即返回none ,可以定义token，用户名等等（yield即完成了teardown的操作，也可以拿到返回值）
    # teardown操作
    print("完成登出操作")

def test_search():
    print("搜索")

def test_cart(login):
    token,username = login
    # print(f"token：{login}") #获取单个参数
    print(f"token：{token},username：{username}")
    # login 返回none
    print("购物车")

def test_order(login):
    # login()
    print("订单")

