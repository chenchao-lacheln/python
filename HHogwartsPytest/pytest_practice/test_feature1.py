import pytest

def test_search(start_app):
    print("搜索功能")

def test_cart():
    print("添加购物车功能")


def test_order(login):
    #提前登录
    print("下单功能")



@pytest.fixture(params=[[1,1,1],[1,2,2],[1,2,3]],ids=['a','b','c'])
# request 特殊用法，可以返回我们的测试数据
def get_param(request):
    print("fixture param")
    return request.param

def test_fixture_param(get_param):
    a = get_param[0]
    b = get_param[1]
    c = get_param[2]
    print(f"a={a},b={b},c={c}")
    print("aaa")