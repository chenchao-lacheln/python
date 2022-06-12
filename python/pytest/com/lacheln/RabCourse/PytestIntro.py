#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 02:47
# @Author  : Lacheln
"""
1.pytest支持简单的单元测试和复杂的功能测试
2.pytest可以结合requests实现接口自动化；结合selenium（web测试框架）、appium（app测试框架）实现自动化功能测试
3.使用pytest结合Allure继承到Jenkins中实现持续继承
4.pytest支持315种以上软件
5.其他场景：添加命令行参数，改变默认编码格式，完成特殊业务场景设置，可以通过pytest的Hook，自己开发插件，满足特殊需求

为什么选择pytest？
丰富的第三方插件
    报告
    多线程
    顺序控制
    兼容unittest
    定制化插件开发

安装
    前提：已配置python环境（python > 3.6V，3.6自带pip）
    第一种方式：pip install pytest  /  pip install -U pytest （-u在已有版本上进行更新）
    pycharm直接安装

python3 和pip3 配置本地默认

"""