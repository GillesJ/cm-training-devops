import pytest

from math_api.math import operations


def test_div_positive():
    assert operations.div(600, 2)


def test_div_t1_negative():
    assert operations.div(-6, 2) == -3

def test_div_by_zero():
    with pytest.raises(ValueError):
        operations.div(1, 0)
