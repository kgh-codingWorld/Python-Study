import pytest
from type_basic import calculate_average,merge_dictionaries,find_user_by_id

# 기본 타입 어노테이션
def test_calculate_average():
    # calculate_average 테스트
    assert calculate_average([1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0
    assert calculate_average([10.5, 20.5]) == 15.5
    
    with pytest.raises(ValueError):
        calculate_average([])

def test_merge_dictionaries():
    # merge_dictionaries 테스트
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged = merge_dictionaries(dict1, dict2)
    assert merged == {"a": 1, "b": 3, "c": 4}

def test_find_user_by_id():
    # find_user_by_id 테스트
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    assert find_user_by_id(users, 2) == {"id": 2, "name": "Bob"}
    assert find_user_by_id(users, 4) is None
