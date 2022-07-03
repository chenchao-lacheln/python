#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 01:56
# @Author  : Lacheln
import pytest




# 测试用例的名字
# 测试用例的路径

@pytest.mark.parametrize("name",["哈利波特","郝敏"])
def test_case1(name):
    print(f"name:{name}")

# def test_case2():
#     print("case2")
#
# def test_case3():
#     print("case3")