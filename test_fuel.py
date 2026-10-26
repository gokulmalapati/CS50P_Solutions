from fuel import convert
from fuel import gauge
import pytest


def test_convert():
    assert convert("10/20") == 50
    assert convert("10/19") == 53
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    with pytest.raises(ValueError):
        convert("-10/11")
    with pytest.raises(ValueError):
        convert("10/9")


def test_gauge():
    assert gauge(2) == "2%"
    assert gauge(1) == "E"
    assert gauge(54) == "54%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"

