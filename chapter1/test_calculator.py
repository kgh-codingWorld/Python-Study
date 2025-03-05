# test_calculator
import pytest
from calculator import add,subtract,multiply,divide,power

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(3, 2) == 9
    
