#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 03:07
# @Author  : Lacheln


'''Allure的用法'''

# 场景:添加日志，附件截图，链接，描述信息，标题
# 常用的方法
    # @alure.epic()           epic描述       定义项目、当有多个项目是使用。往下是Feature
    # @allure.feature()       模块名称        用例按照模块区分，有多个模块时给每个起名字
    # @allure.story()         用例名称        用例的描述（用例成功和失败的用例）
    # @allure.title           用例标题        用例标题
    # @allure.testcase()      用例相关链接     自动化用例对应的功能用例存放系统的地址
    # @allure.issue()         缺陷地址         对应缺陷管理系统里边的缺陷地址
    # @allure.description()   用例描述         对测试用例的详细描述
    # @allure.step()          操作步骤         测试用例的操作步骤（用例比较复杂的时候，出错方便排查）
    # @allure.severity()      用例等级         blocker、critical 、normal、minor、trivial
    # @allure.link()          定义连接         用于定义一个需要在测试报告中展示的连接
    # @allure.attachment()    附件             添加测试报告附件
