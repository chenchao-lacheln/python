#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/25 20:15
# @Author  : Lacheln

from learn.pytest1.live_course.scrip.calculator import Calculator
from learn.pytest1.live_course.test.utils.log_utils import logger


class Base:
    def setup_class(self):
        # 实例化
        # 在base层写入日志
        logger.info("实例化 calc 对象")
        self.cal = Calculator()

    def setup(self):
        logger.info("开始计算")
        # print("开始计算")

    def teardown(self):
        logger.info("结束计算")
        # print("结束计算")

