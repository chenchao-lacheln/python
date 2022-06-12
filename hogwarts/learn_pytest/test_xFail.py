import pytest

# xFail也可以在代码中使用
# 进度条：pytest 01:33:50
def test_xfail():
    print("******开始测试******")
    pytest.xfail(reason = "该功能尚未完成")
    print("测试过程")
    assert 1 == 1


# 场景：当前case，但是bug还没有解决，使用xFail仍然会执行该条case，失败则展示xfail，成功则展示xpass
@pytest.mark.xfail
def test_aaaa():
    print("test_xfail 方法执行")
    assert 2 == 2

xfail = pytest.mark.xfail

@xfail(reason = "bug 110")
def test_hello4():
    assert 0
