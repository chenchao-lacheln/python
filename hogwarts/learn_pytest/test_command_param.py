import pytest


def double(a):
    return a * 2

@pytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)

@pytest.mark.float
def test_double_minus():
    print("test double minus")
    assert -2 == double(-1)

@pytest.mark.float
def test_double_float():
    assert 0.21 == double(0.1)

@pytest.mark.zero
def test_double_0():
    assert 0 == double(0)

@pytest.mark.bignum
def test_double_bignum():
    assert 200 == double(100)

@pytest.mark.str
def test_double_str():
    assert "aa" == double("a")

@pytest.mark.str
def test_double_str1():
    assert "a$a$" == double("a$")

if __name__ == '__main__':
    # 1.运行当前目录下所有用例
    # pytest.main()
    # pytest.main('./')
    # # 2.运行test.mark1.py::test_dke模块中的某一条用例
    # pytest.main(['test_mark1.py::test_dke','-vs'])
    pytest.main(['test_setup_setdowm.py::TestDemo','-vs'])
    # # 3.运行某个标签
    # pytest.main(['test_mark1.py','-vs','-m','dke'])

