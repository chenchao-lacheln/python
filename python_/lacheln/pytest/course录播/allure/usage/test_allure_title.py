#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 03:19
# @Author  : Lacheln

'''设置标题'''

import allure
class TestSearch():
    @allure.title("ios")
    def test_case1(self):
        print("case1")

    @allure.title("android")
    def test_case2(self):
        print("case2")