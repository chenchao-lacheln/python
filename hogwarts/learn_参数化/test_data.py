# #无参数化,重复的，大量的内容和数据
#
# class TestData():
#     def test_data1(self):
#         a=10
#         b=20
#         print(a+b)
#
#     def test_data2(self):
#         a=11
#         b=28
#         print(a+b)
#
#     def test_data3(self):
#         a=14
#         b=22
#         print(a+b)
import pytest
#
#
import yaml


class TestData():
#     #string
    @pytest.mark.parametrize('a,b',yaml.safe_load(open("./data.yaml")))
    #tuple
    # @pytest.mark.parametrize(('a','b'),[(1,2),(3,4),(5,6)])
    #list
    # @pytest.mark.parametrize(['a','b'],[(1,2),(3,4),(5,6)])

    def test_data1(self,a,b):
        print(a+b)


import pytest
import yaml

class TestData():
#     #string
    @pytest.mark.parametrize('a,b',yaml.safe_load(open("./data.yaml")))
    def test_data1(self,a,b):
        print(a+b)