#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/2 18:17
# @Author  : Lacheln
import os

import yaml

def test_load():
    # with 执行完代码块后，会自动关闭文件
    with open("../datas/demo.yaml") as f:
        # safe_load()将yaml格式转成python对象
        result = yaml.safe_load(f)
    print(result)

'''
将yaml格式转成python对象
'''
def load_adddata(name,level):
    '''
    :param name: 用例范围
    :param level:级别
    :return:
    '''
    # with 执行完代码块后，会自动关闭文件
    with open("../datas/test_add_data.yaml",encoding="utf-8") as f:
        # safe_load()将yaml格式转成python对象
        result = yaml.safe_load(f)
    print(result)
    # P0测试数据
    data = result.get(name).get(level).get('data')
    # P0测试用例别名
    ids = result.get(name).get(level).get('ids')
    print(f"测试数据 = {data}",f"\n测试用例别名 = {ids}")
    return data,ids

def test_getdata_params():
    load_adddata("add", "P0")
'''
safe_dump()将python对象转换成 yaml对象
'''
def test_dump():
    # safe_dump()将python对象转换成 yaml对象
    data = {"add":[[98.99, 99, 197.99],
                   [99, 98.99, 197.99],
                   [-98.99, -99, -197.99],
                   [-99, -98.99, -197.99],
                   [99.01, 0, '参数大小超出范围'],
                   [2, 99.01, '参数大小超出范围'],
                   [2, 99.01, '参数大小超出范围'],
                   [1, -99.01, '参数大小超出范围']
                   ]}
    # 报错：FileNotFoundError: [Errno 2] No such file or directory: 'python_data.yaml' （没有创建文件夹-->>创建一个yaml文件即可）
    # 报错：io.UnsupportedOperation: not writable（没有写入权限 -->> 添加权限 mode='w'）
    # python对象有中文的时候，需要添加 allow_unicode=True 否则写入yaml文件的数据是乱码
    with open("../datas/python_data.yaml",mode='w',encoding="utf-8") as f:
        yaml.safe_dump(data,f,allow_unicode=True)

def test_path():
    # 绝对路径 路径+文件名
    # __file__ python内置变量，代表当前变量
    # os.path.abspath 获取绝对路径 （路径+文件名）
    # os.path.dirname 获取路径 （路径 不包含文件名）
    # os.path.join 拼接路径

    path = os.path.abspath(__file__)
    print(path)
    print(os.path.dirname(path))
    demo_path = os.path.dirname(path)
    yaml_path = "datas/test_add_data.yaml"
    yaml_finalpath = os.path.join(demo_path,"../",yaml_path)
    print(yaml_finalpath)
    with open(yaml_finalpath) as f:
        result = yaml.safe_load(f)
        print(result)