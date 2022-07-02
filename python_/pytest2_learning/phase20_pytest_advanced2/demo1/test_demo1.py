#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 00:39
# @Author  : Lacheln
import pytest


@pytest.mark.run(order=2)
# @pytest.mark.second
def test_foo():
    assert True

@pytest.mark.run(order=1)
# @pytest.mark.first
def test_bar():
    assert True
