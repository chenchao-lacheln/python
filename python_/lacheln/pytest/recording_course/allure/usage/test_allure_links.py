#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 23:22
# @Author  : Lacheln

'''
场景:
测试报告中，添加用例的链接，bug 链接地址，相关的链接地址
解决:
@allure.link()、@allure.issue()、 @allure.testcase()
主要是为了将allure报告和测试管理系统集成(用例管理/bug管理)， 可以更快速的跳转到公司内部地址。
'''
import allure

TEST_CASE_LINK = "https://www.baidu.com/"

@allure.link("https://www.baidu.com/")
def test_with_link():
    pass

@allure.link("https://www.baidu.com/",name="百度地址")
def test_with_named_link():
    pass

@allure.issue("140","BUG地址")
def test_with_issure_link():
    pass

@allure.testcase(TEST_CASE_LINK,"测试管理管理平台地址")
def test_with_testcase_link():
    pass
