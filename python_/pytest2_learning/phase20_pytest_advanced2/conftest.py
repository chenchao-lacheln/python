#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 01:45
# @Author  : Lacheln
from typing import Optional, List

import pytest
import yaml


def pytest_runtest_setup(item: "Item") -> None:
    print("hook : setup")

def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    print("hook : teardown")


# # 修改默认编码
# # 收集完测试用例之后 被调用的hook函数
# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     print(items)
#     # name 名字
#     # nodeid 测试用例的路径
#     # 含有中文的测试用例的名字，改写编码格式
#     for item in  items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#     # 收集上来的用例是一个List
#     items.reverse() # 通过 reverse() 方法 可以颠倒执行顺序，将列表进行反转
    


def pytest_addoption(parser):
    mygroup = parser.getgroup("lacheln") #group 将下面所有的option 都展示在这个group下
    mygroup.addoption("--env",  #注册一个命令行选项
                      default = "test", #参数默认值
                      dest = "env",    #存储的变量，为属性命令，可以使用Option对象访问这个值，
                      help = "set your run env" # 帮助信息，参数的描述信息
                      )

# 如果针对传入的不同参数完成不同的逻辑处理
# @pytest.fixture(scope='session')
# def cmdoption(request):
#     result =  request.config.getoption("--env")
#     return result

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env",default="test")
    if myenv =='test':
        datapath = "datas/test/data.yml"
    elif myenv == 'dev':
        datapath = "datas/dev/data.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return myenv,datas
