#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 22:06
# @Author  : Lacheln
import csv

import pytest



def get_csv():

    with open('../data/demo.csv') as file:
        raw = csv.reader(file)

        data = []
        for line in raw:
            data.append(line)
            print(data)
    return data


class TestWithCSV:
    @pytest.mark.parametrize('x,y,expected',get_csv())
    def test_add(self,x,y,expected):
        assert x,y == expected