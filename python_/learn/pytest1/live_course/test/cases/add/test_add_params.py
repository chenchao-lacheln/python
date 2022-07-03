#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 01:12
# @Author  : Lacheln


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
import allure

import pytest
import sys
# sys.path.append('../../../../../..')
import yaml

from learn.pytest1.live_course.test.conftest import get_adddata
from learn.pytest1.live_course.test.utils.log_utils import logger

sys.path.append('../../../../../..')

from learn.pytest1.live_course.test.base.base import Base





def teardown_module():
    # 清理数据
    print("结束测试")


# 继承
# 安装java，安装allure 安装allure-pytest1
@allure.feature("相加功能")
class TestAdd(Base):
    add_P0_data = get_adddata("add","P0")[0]
    add_P0_ids = get_adddata("add","P0")[1]

    @allure.story("相加P0级别用例")
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect",[[1,2,3],
                                           [10, 0.02,10.02],
                                           [98.99, 99,197.99],
                                           ],
                             ids=["int1","float1","int_float1"])
    # 参数化，当测试步骤完全一样，测试数据不一样的时候，就可以使用参数化
    def test_add1(self,a,b,expect):
        # 添加代码日志，且日志会同时输出到报告当中
        logger.info(f"输入数据:{a},{b},期望结果:{expect}")
        #测试步骤：一些关键步骤，相加的操作，可以添加步骤
        with allure.step("step1：相加操作"):
            result = self.cal.add(a,b)
        logger.info(f"实际结果:{result}")
        # expect = 3
        # 增加附件
        allure.attach.file("/Users/lacheln/PycharmProjects/python_/learn/pytest1/live_course/test/img/lacheln.png",
                           name="计算完成截图")
        with allure.step("step2:断言"):
            assert result == expect

    # @pytest1.mark.P0
    # def test_add2(self):
    #     result = self.cal.add(-0.01, 0.02)
    #     expect = 0.01
    #     assert result == expect
    #
    # @pytest1.mark.P0
    # def test_add3(self):
    #     result = self.cal.add(10, 0.02)
    #     expect = 10.02
    #     assert result == expect

    @allure.feature("相加P1级别用例")
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect",add_P0_data,ids=add_P0_ids)
    def test_add4(self,a,b,expect):
        logger.info(f"输入数据:{a},{b},期望结果:{expect}")
        with allure.step("step1:相加操作"):
            result = self.cal.add(a, b)
        # expect = 197.99
        with allure.step("step2：断言"):
            assert result == expect
        logger.info(f"实际结果:{result}")

    # @pytest1.mark.P1
    # def test_add5(self):
    #     result = self.cal.add(99, 98.99)
    #     expect = 197.99
    #     assert result == expect
    #
    # @pytest1.mark.P1
    # def test_add6(self):
    #     result = self.cal.add(-98.99, -99)
    #     expect = -197.99
    #     assert result == expect
    #
    # @pytest1.mark.P1
    # def test_add7(self):
    #     result = self.cal.add(-99, -98.99)
    #     expect = -197.99
    #     assert result == expect

    #
    # @pytest1.mark.P1
    # @pytest1.mark.parametrize("a,b,expect",[[99.01, 0,"参数大小超出范围"],
    #                                        [2, 99.01,"参数大小超出范围"],
    #                                        [2, 99.01,"参数大小超出范围"],
    #                                        [1, -99.01,"参数大小超出范围"],
    #                                        ],
    #                          ids=["int_float6","int_float7","int_float8","int_float9"])
    # def test_add8(self,a,b,expect):
    #     result = self.cal.add(a, b)
    #     # expect = "参数大小超出范围"
    #     assert result == expect

    # @pytest1.mark.P1
    # def test_add9(self):
    #     result = self.cal.add(-99.01, -1)
    #     expect = "参数大小超出范围"
    #     assert result == expect
    #
    # @pytest1.mark.P1
    # def test_add10(self):
    #     result = self.cal.add(2, 99.01)
    #     expect = "参数大小超出范围"
    #     assert result == expect
    #
    # @pytest1.mark.P1
    # def test_add11(self):
    #     result = self.cal.add(1, -99.01)
    #     expect = "参数大小超出范围"
        assert result == expect

    @allure.feature("相加P1级别特殊处理用例")
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect",[["文",9.3,"TypeError"]],
                             ids=["chinese"])
    def test_add12(self,a,b,expect):
        logger.info(f"输入数据:{a},{b},预期结果:{expect}")
        #第一种方式
        # try:
        #     result = self.cal.add("文", 9.3)
        # except TypeError as e:
        #     print(e)

        #第二种方式 pytest1.raises 捕获异常
        # eval(）方法 可以将str类型的转化为可执行的类别，
        # 比如"1+1"进行输入是一个字符串，结果仍然是"1+1"，
        # 但是eval("1+1")，进行运算，结果就等于2，
        # 实现数据的时候，yaml是不支持TypeError这种错误类型的，
        # 所以需要加上双引导"TypeError"，转化为str类型的，再通过eval(expect)方法转换成可执行的表达式
        with pytest.raises(eval(expect)) as e:
            result = self.cal.add(a,b)
            logger.info(f"实际结果:{result}")

