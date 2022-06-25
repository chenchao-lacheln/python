#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 2:11 下午
# @Author  : Lacheln

"""
文件名：test_first.py
类名：TestDemo
方法明：test_demo
"""

def answer(x):
    return x + 1

def test_answer():
    assert answer(1) == 5

class TestDemo:
    def test_demo(self):
        pass
