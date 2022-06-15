#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 9:40 下午
# @Author  : Lacheln

"""
运行测试用例
"""

'''
1.执行包下所有的用例: pytest/py.test [包名]
2.执行单独一个pytest模块: pytest 文件名.py
3.运行某个模块里面某个类:pytest文件名.py::类名
4.运行某个模块里面某个类里面的方法: pytest文件名.py::类名::方法名:
'''

"""
场景：执行失败的测试用例
命令行参数-使用缓存状态
"""
'''
--1f(--last-failed)只重新运行故障。
--ff(--failed- first) 先运行故障然后再运行其余的测试
'''
# pytest
