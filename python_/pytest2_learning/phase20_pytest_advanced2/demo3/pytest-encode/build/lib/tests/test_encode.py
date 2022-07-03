#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 01:38
# @Author  : Lacheln
import pytest


@pytest.mark.parametrize("name",["哈利波特","郝敏"])
def test_case1(name):
    print(f"name:{name}")