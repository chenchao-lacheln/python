# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: conftest.py
# @Author: lacheln
# @Time: 9月 07, 2021
# ---
import time
from typing import List

import pytest

from pytest_practice.pythoncode.calculator import Calculator


# # 查看当前的系统的路径有哪些
# import sys
# print(sys.path)


@pytest.fixture(autouse=True)
def start_app():
    print('启动Appa操作')

@pytest.fixture(autouse=True)
def login():
    print('登录操作')

#使用yield模拟teardown
@pytest.fixture(autouse=True)
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 遍历所有的测试用例，把用例的中文都转成unicode-escape格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 日志文件按时间生成，自动生成
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    # time导报不要导错了import time
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # # rootdir获取项目的根路径，是根据一下两个文件来获取的
    #优先级1、pytest.ini所在的路径
    #优先级2、conftest.py所在的路径
    #如果两个文件都没有，则会报错
    rootdir = request.config.rootdir
    print(rootdir)
    # 日志地址写死，想把日志放在根路径
    log_name = 'output/log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)