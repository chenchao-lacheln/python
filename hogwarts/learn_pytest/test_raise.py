import pytest

def test_raise():
    # 预期ValueError异常，但是抛出的是除数为0的异常
    with pytest.raises((ZeroDivisionError,ValueError)):
        # raise ValueError("value must be 0 or None")
        raise ZeroDivisionError("除数为0")
def test_raise1():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"