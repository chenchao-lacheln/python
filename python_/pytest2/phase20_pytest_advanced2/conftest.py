#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 01:45
# @Author  : Lacheln
from typing import Optional, List


def pytest_runtest_setup(item: "Item") -> None:
    print("hook : setup")

def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    print("hook : teardown")


# 收集完测试用例之后 被调用的hook函数
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    pass