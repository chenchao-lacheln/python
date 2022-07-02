#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 01:43
# @Author  : Lacheln


import pytest

'''登录操作'''

# @pytest.fixture(scope="session") # session级别，在整个会话的开始和结束 执行
@pytest.fixture(scope="function",autouse=True)
def login():
    # setup操作
    print("完成登录操作")
    token  = "adsadadsdasfas"
    username = "jhkjfdjskf"
    yield token,username
    # teardown操作
    print("完成登出操作")