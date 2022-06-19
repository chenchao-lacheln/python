#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 02:47
# @Author  : Lacheln

import pytest

# pip install allure-pytest
def test_success():
    assert True

def test_fail():
    assert False

def test_skip():
    pytest.skip("for a reason!")

def test_broken():
    raise Exception('oops')