#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 22:59
# @Author  : Lacheln

'''
场景:
测试过程中每个步骤，一 般放在具体逻辑方法中，可以放在关键步骤中，在报告中显示
在app, web自动测试当中，建议每切换到一个新的页面当做一个step
解决:
with allure.step():可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
'''

import allure


@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤一：打开应用"):
            print("打开应用")
        with allure.step("步骤二：进入登录页面"):
            print("登录页面")
        with allure.step("步骤三：输入用户信息"):
            print("输入用户名和密码")
        with allure.step("步骤四：进入成功页面"):
            print("这是登录测试用例，登录成功")



