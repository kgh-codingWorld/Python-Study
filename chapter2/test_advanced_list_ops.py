import pytest
from advanced_list_ops import custom_map, custom_filter, custom_reduce

# 고급 리스트 연산 테스트
def test_custom_map():
    # custom_map 테스트
    assert custom_map(lambda x: x * 2, [1, 2, 3, 4]) == [2, 4, 6, 8]
    assert custom_map(str, [1, 2, 3]) == ["1", "2", "3"]
    
def test_custom_filter():
    # custom_filter 테스트
    assert custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert custom_filter(lambda x: x > 10, [5, 15, 3, 20]) == [15, 20]

def test_custom_reduce():
    # custom_reduce 테스트
    assert custom_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) == 15
    assert custom_reduce(lambda x, y: x * y, [1, 2, 3, 4], 2) == 48
    
    with pytest.raises(ValueError):
        custom_reduce(lambda x, y: x + y, [])