#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 01:12
# @Author  : Lacheln

# 测试相加方法
import pytest

from lacheln.pytest.live_course.scrip.calculator import Calculator

'''
测试用例编写
●题目:
    根据需求编写计算机器(加法和除法)相应的测试用例
    在调用每个测试方法之前打印[开始计算]
    在调用测试方法之后打印[结束计算]
    调用完所有的测试用例最终输出[结束测试]
    为用例添加标签
●注意:
    a、使用等价类，边界值，错误猜测等方法进行用例设计
    b、用例中要添加断言，验证结果
    C、灵活使用测试装置
'''

def teardown_module():
    # 清理数据
    print("结束测试")

# 封装
class Base:

    def setup_class(self):
        # 实例化
        self.cal = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

# 继承
class TestAdd(Base):

    @pytest.mark.P0
    def test_add1(self):
        result = self.cal.add(1,2)
        expect = 3
        assert result == expect

    @pytest.mark.P0
    def test_add2(self):
        result = self.cal.add(-0.01, 0.02)
        expect = 0.01
        assert result == expect

    @pytest.mark.P0
    def test_add3(self):
        result = self.cal.add(10, 0.02)
        expect = 10.02
        assert result == expect

    @pytest.mark.P1
    def test_add4(self):
        result = self.cal.add(98.99, 99)
        expect = 197.99
        assert result == expect

    @pytest.mark.P1
    def test_add5(self):
        result = self.cal.add(99, 98.99)
        expect = 197.99
        assert result == expect

    @pytest.mark.P1
    def test_add6(self):
        result = self.cal.add(-98.99, -99)
        expect = -197.99
        assert result == expect

    @pytest.mark.P1
    def test_add7(self):
        result = self.cal.add(-99, -98.99)
        expect = -197.99
        assert result == expect

    @pytest.mark.P1
    def test_add8(self):
        result = self.cal.add(99.01, 0)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add9(self):
        result = self.cal.add(-99.01, -1)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add10(self):
        result = self.cal.add(2, 99.01)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add11(self):
        result = self.cal.add(1, -99.01)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add12(self):
        #第一种方式
        # try:
        #     result = self.cal.add("文", 9.3)
        # except TypeError as e:
        #     print(e)

        #第二种方式 pytest.raises 捕获异常
        with pytest.raises(TypeError) as e:
            result = self.cal.add("文",9.3)
