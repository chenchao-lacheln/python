#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/2 17:20
# @Author  : Lacheln

'''使pytest支持中文'''
import os
import sys
from typing import List

import pytest
import yaml

# sys.path.append('../../')
from learn.pytest1.live_course.test.utils.log_utils import logger

'''编码格式改写，兼容中文格式'''
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
    items.reverse() # 通过 reverse() 方法 可以颠倒执行顺序，将列表进行反转

'''获取yaml 数据'''
def get_adddata(name,level):
    # 读取文件通过相对路径的话，相对路径通常在根目录运行项目的时候，会报错路径不对
    # os.path.abspath()
    # with open("../../datas/test_add_data.yaml",encoding="utf-8") as f:

    # 调用获取绝对路径的方法get_yaml_path()
    with open(get_yaml_path(),encoding="utf-8") as f:
        # safe_load()将yaml格式转成python对象
        result = yaml.safe_load(f)
    print(result)
    # P0测试数据
    data = result.get(name).get(level).get('data')
    # P0测试用例别名
    ids = result.get(name).get(level).get('ids')
    print(f"测试数据 = {data}",f"\n测试用例别名 = {ids}")
    return data,ids

'''通过绝对路径获取到yaml文件的路径'''
def get_yaml_path():
    # __file__ == util.py
    path = os.path.abspath(__file__)
    demo_path = os.path.dirname(path)
    yaml_path = "datas/test_add_data.yaml"
    yaml_finalpath = os.path.join(demo_path,"../",yaml_path)
    return yaml_finalpath


'''清理测试数据'''
# autouse=True 自动执行
# scope="session"作用域
# yield 前相当于setup 后相当于teardown
@pytest.fixture(autouse=True,scope="session")
def clear_datas():
    yield
    logger.info("清理所有的测试数据")