# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: test_calc.py
# @Author: lacheln
# @Time: 9月 07, 2021
# ---
import pytest
import yaml

#读取测试数据calc.yaml
#pip install pyyaml
# 1.先定义数据文件
# 2.定义一个方法,读取这个文件内容，return想要的数据格式
def get_datas():
    # with会打开这个文件，然后自动关闭这个文件
    with open("datas/calc.yml") as f:
    #safe_load将yaml文件转成python对象的过程;safe_dump是将python对象（字典、列表）保存到yaml文件中
    # yaml.safe_dump()
        datas = yaml.safe_load(f)
    #读取yaml文件里面的数据
    get_int_datas = datas.get("add").get("int").get("datas")
    get_int_ids = datas.get("add").get("int").get("ids")

    return(get_int_datas,get_int_ids)

# 思考题
def get_datas1():
    with open("datas/calc.yml") as f:
        # datas = yaml.safe_load(f)
        # 换成下面的方式可不可以
        get_int_datas = yaml.safe_load(f).get("add").get("int").get("datas")
        get_int_ids = yaml.safe_load(f).get("add").get("int").get("ids")
    #组装成想要的数据格式
    return(get_int_datas,get_int_ids)

def test_getdatas():
    print(get_datas())

class TestCalc():
    #get_datas()[0],ids=get_datas()[1] 第二组数据需要用ids指定到该数据
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[1])
    def test_add(self,a,b,expect,get_calc):
        result = get_calc.add(a,b)
        assert result == expect

    def test_div(self,get_calc):
        result = get_calc.div(4,2)
        assert result == 2

# 如果测试用例需要传入参数
# @pytest.mark.parametrize('a,b',[
#     [1,2],[3,4],[5,6]
# ])
# def test_paams(a,b):
#     print("传参数用例")