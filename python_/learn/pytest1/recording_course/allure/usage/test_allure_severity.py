#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 23:53
# @Author  : Lacheln

'''
五种级别:
BLOCKER("blocker") 阻塞缺陷(功能未实现，无法下一步)
CRITICAL(”critical") , 严重缺陷(功能点缺失)
NORMAL ("normal"), 一般缺陷(边界情况，格式错误)
MINOR ("minor"),次要缺陷 (界面错误与ui需求不符)
TRIVIAL("trivial") ; 轻微缺陷(必须项无提示，或者提示不规范)
'''

'''
场景:
通常测试有PO、冒烟测试、验证上线测试。
按重要性级别来分别执行的，比如上线要把主流程和重要模块都跑一遍
解决:
也可以通过allure.severity来附加标记
实例:
在方法，函数和类上面加 @allure.severity(allure.severity_level.TRIVIAL)
运行:
运行级别为: normal,critical 的测试用例
pytest1 -s -v文件名-allure-severities=normal,critical -alluredir-./result
pytest1 test_allure_severity.py  --allure-severities=critical,normal --alluredir ./result 
'''

import allure

@allure.severity(allure.severity_level.BLOCKER)
def test_with_no_severity_label( ):
    pass

@allure. severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity( ):
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):
    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL )
    def test_inside__thesnormal_severity__test_class__with_overridingcritical_severity(self):
        pass