import pytest

@pytest.mark.parametrize("wb",["appnium","selenium","pytest"])
@pytest.mark.parametrize("code",["UTF_8","GBK","GB2312"])
def test_dke(wb,code):
    print(f"wb:{wb},code:{code}")