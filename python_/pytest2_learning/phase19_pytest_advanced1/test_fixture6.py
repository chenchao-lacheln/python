#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 02:04
# @Author  : Lacheln

import  pytest
"""fixture参数化"""

# 添加多组用户名和密码
@pytest.fixture(params=["Marry","Tom"])
def login(request): # request固定参数用法
    print(f"用户名:{request.param}") # request.param固定用法
    return request.param


def test_case1(login):
    print(f"case1：数据为：{login}")
