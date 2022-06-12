import pytest

#多个测试用例
search_list = ['appnuim','selenium','pytest']

#参数名和变量名要对应上
# @pytest.mark.parametrize实现参数化的装饰器功能
@pytest.mark.parametrize('name',search_list) #参数名字放在第一个位置，第二个位置放置参数列表 name（变量名）
def test_search(name): #传递一个参数，name（参数名）
    assert name in search_list