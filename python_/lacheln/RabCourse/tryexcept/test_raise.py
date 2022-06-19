#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 01:39
# @Author  : Lacheln
import pyDemo


def test_raise1():
    with pyDemo.raises(ValueError):
        raise ValueError("must be 0 or none")

def test_raise2():
    with pyDemo.raises(ValueError) as rename:
        raise ValueError("must be 0 or none")
    assert rename.type is ValueError
    assert  rename.value.args[0] == "must be 0 or none"