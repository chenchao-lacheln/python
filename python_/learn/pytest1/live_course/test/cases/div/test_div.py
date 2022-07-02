#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/2 16:36
# @Author  : Lacheln
import pytest

from learn.pytest1.live_course.test.base.base import Base


class TestDiv(Base):
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect",[[1,1,1],
                                           [-0.01,-0.02,0.5],
                                           [-0.01,0.02,-0.5],
                                           [10,0.02,500],
                                           ],ids=["2个整数","2个浮点数","2个浮点数-正负","整数和浮点数"])
    def test_div1(self,a,b,expect):
        result = self.cal.div(a,b)
        assert result == expect

    # def test_div2(self):
    #     datas = [[1,1,1],
    #             [-0.01,-0.02,0.5],
    #              [-0.01,0.02,-0.5],
    #              [10,0.02,500],
    #              ]
    #     # 问题：一旦其中某一条数据对应的用例错误，后面的测试数据将不再执行
    #     for data in datas:
    #         result = self.cal.div(data[0], data[1])
    #         assert result == data[2]

    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect",[[99,0,"ZeroDivisionError"]],ids=["除数为0"])
    def test_div2(self,a,b,expect):
        with pytest.raises(eval(expect)) as e:
            result = self.cal.div(a,b)
            assert result == expect
