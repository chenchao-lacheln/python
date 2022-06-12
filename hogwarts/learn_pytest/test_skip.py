# 代码中添加 跳过代码块 pytest.skip(reason="")
import pytest

@pytest.mark.skip(reason="存在bug") #跳过整个测试用例
def test_aaa():
    assert True

@pytest.mark.skip(reason="代码没有实现")
def test_bbb():
    assert True


def check_login():
    return False

def test_function():
    print("start")
    # 场景：单个测试用例，添加判断预期，如果未登录(False)，则跳过后续步骤,登录（True）则不会跳过
    if not check_login():
        pytest.skip("unsupported configuration")
    print("end")