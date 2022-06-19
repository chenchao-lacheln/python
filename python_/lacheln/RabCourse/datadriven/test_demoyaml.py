#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 01:56
# @Author  : Lacheln
import pytest
import yaml




# python3.X只能使用pip install pyyaml 来安装。
class TestYaml_:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_yaml_(self,env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的IP = ",env['test'])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的IP = ", env['dev'])