#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 01:37
# @Author  : Lacheln


# 修改默认编码
# 收集完测试用例之后 被调用的hook函数
from typing import List


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    # name 名字
    # nodeid 测试用例的路径
    # 含有中文的测试用例的名字，改写编码格式
    for item in  items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    # 收集上来的用例是一个List
    items.reverse()