import pytest

#多参数
"""
1、参数化的名字，要与方法中的参数命，一一对应
2、如果传递多个参数的话，要放在列表中，列表中嵌套列表 / 元祖
3、ids可以为测试用例重命名，ids的个数 == 传递的数据的个数
"""

@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),("2+5",7),("7+5",12)
],ids=['number1','number2','number3'])
def test_mark_more(test_input,expected):
    #eval可以将字符串的表达式转化为实际的表达式
    assert eval(test_input) == expected
