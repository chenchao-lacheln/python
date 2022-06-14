#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 1:35 下午
# @Author  : Lacheln

'''
●这是pytest的内置标签，可以处理-些特殊的测试用例，不能成功的测试用例
●skip -始终跳过该测试用例
●skipif -遇到特定情况跳过该测试用例
●xfail 遇到特定情况,产 生个“期望失败’ 输出
'''
import sys

import pytest

'''
Skip使用场景
●调试时不想运行这个用例
●标记无法在某些平台上运行的测试功能
●在某些版本中执行，其他版本中跳过
比如:当前的外部资源不可用时跳过
    如果测试数据是从数据库中取到的，
    ■连接数据库的功能如果返回结果未成功就跳过，因为执行也都报错
●解决1:添加装饰器
    @pytest.mark.skip
    @pytest●mark.skipif
●解决2:代码中添加跳过代码
    ■pytest.skip( reason)
'''

@pytest.mark.skip
def test_a():
    print("代码未开发完")
    assert True

@pytest.mark.skip(reason = "代码没有实现")
def test_b():
    assert True

#判断是否登录 进行跳过

def check_login():
    return False
def test_login():
    print("start")
    if not check_login():
        pytest.skip("not login")
    print("end")

#pytest.mark.skipif()

print(sys.platform)
@pytest.mark.skipif(sys.platform == "mac",reason="dose not run on mac")
def test_platform():
    assert True

@pytest.mark.skipif(sys.version == (3,5),reason="requires python3.6 or higher")
def test_version():
    assert True

'''
●与skip类似，预期结果为fail，
标记用例为fail 
用法:添加装饰器@pytest.mark.xfail
'''

#XFAIL
@pytest.mark.xfail
def test_xfail():
    assert 1 == 2

#XPASS
@pytest.mark.xfail
def test_xfail():
    assert 1 == 1