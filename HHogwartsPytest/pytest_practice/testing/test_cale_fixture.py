# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: test_cale_fixture.py
# @Author: lacheln
# @Time: 9月 08, 2021
# ---
import logging
import time

import allure
import pytest
import yaml

#读取测试数据calc.yaml
#pip install pyyaml
# 1.先定义数据文件
# 2.定义一个方法，读取这个文件的内容，return想要的数据格式
def get_datas1():
    with open("datas/calc.yml") as f:
    #safe_load将yaml文件转成python对象的过程;safe_dump是将python对象（字典、列表）保存到yaml文件中
    # yaml.safe_dump()
        datas = yaml.safe_load(f)
    #读取yaml文件里面的数据
    get_int_datas = datas.get("add").get("int").get("datas")
    get_int_ids = datas.get("add").get("int").get("ids")

    return(get_int_datas,get_int_ids)

@pytest.fixture(params=get_datas1()[0],ids=get_datas1()[1])
def get_datas_byfixture(request):
    print(f"request.param == {request.param}")
    return request.param

def test_getdata_fixture(get_datas_byfixture):
    print(get_datas_byfixture)

def test_getdatas():
    print("get_datas()")

# pip install allure-pytest
@allure.feature("计算器")
class TestCalc():
    #get_datas()[0],ids=get_datas()[1] 第二组数据需要用ids指定到该数据
    # @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[1])
    @allure.story("相加功能")
    @pytest.mark.run(order=2)
    def test_add(self,get_calc,get_datas_byfixture):
        logging.info(f"测试相加功能：参数:{get_datas_byfixture}")
        result = get_calc.add(get_datas_byfixture[0],get_datas_byfixture[1])
        assert result == get_datas_byfixture[2]

    @allure.story("相除功能")
    @pytest.mark.run(order=1)#按照顺序执行
    def test_div(self,get_calc):
        logging.info(f"测试相除功能：参数:{4,2,2}")
        result = get_calc.div(4,2)
        assert result == 2

    @allure.story("相减功能")
    @pytest.mark.parametrize("a,b,expect",[[4,2,2]],ids=["减法"])
    def test_jian(self,a,b,expect,get_calc):
        logging.info(f"测试相减功能：参数:{a,b,expect}")
        result = get_calc.jian(a,b)
        assert result ==expect

def test_a():
    time.sleep(1)

def test_b():
    time.sleep(1)

def test_c():
    time.sleep(1)

# 如果测试用例需要传入参数
# @pytest.mark.parametrize('a,b',[
#     [1,2],[3,4],[5,6]
# ])
# def test_paams(a,b):
#     print("传参数用例")