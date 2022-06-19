#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 03:29
# @Author  : Lacheln

# 场景:
'''希望在报告中看到测试功能，子功能或场景'''
# 解决:
# @Feature, @story
# 步骤:
# import allure
# 功能上加@allure.feature(功能名称)
# 子功能上加@allure.story(子功能名称’)
# 运行:
# pytest文件名- allure-features=FEATURES SET --allure-stories=STORIES SET

# feature相当于一个功能，一个 大的模块，相当于testsuite
# story相当于对应这个功能或者模块下的不同场景，分支功能
# feature与story类似于父子关系

import allure

@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    @allure.title("ios")
    def test_case1(self):
        print("case1")

    @allure.story("搜索失败")
    @allure.title("android")
    def test_case2(self):
        print("case2")

@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("打开应用")
        print("登录页面")
        print("输入用户名和密码")
        print("这是登录测试用例，登录成功")

    @allure.story("登录成功")
    def test_login_success_a(self):
        print("这是登录测试用例，登录成功")

    @allure.story("登录成功")
    def test_login_success_b(self):
        print("用户名缺失")



    @allure.story("登录失败")
    def test_login_success(self):
        print("打开应用")
        print("登录页面")
        assert '1' == 1
        print("登录失败")

    @allure.story("登录失败")
    def test_login_failure_b(self):
        print("输入用户名")

