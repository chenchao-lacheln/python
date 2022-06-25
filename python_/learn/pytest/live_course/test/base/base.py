#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/25 20:15
# @Author  : Lacheln

from learn.pytest.live_course.scrip.calculator import Calculator



class Base:
    def setup_class(self):
        # 实例化
        self.cal = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

