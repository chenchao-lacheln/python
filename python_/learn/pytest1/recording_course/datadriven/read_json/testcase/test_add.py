#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 00:05
# @Author  : Lacheln

import json

import pytest



def get_json():
    with open('../data/demo_add.json', 'r') as file:
        data = json.loads(file.read())
        return list(data.values())



class TestWithJson:
    @pytest.mark.parametrize('x,y,expected',get_json())
    def test_add(self,x,y,expected):
        assert x,y == expected
