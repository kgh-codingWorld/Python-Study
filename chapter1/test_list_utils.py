import pytest
from list_utils import find_max, filter_even_numbers, average


def test_find_max():
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([-1, -5, -3]) == -1
    with pytest.raises(ValueError):
        find_max([])

def test_filter_even_number():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([1, 3, 5]) == []

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([10, 20]) == 15.0
        