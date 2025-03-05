# test_chapter2.py
import pytest
from list_processing import remove_empty_strings, add_after_item, replace_item

def test_remove_empty_strings():
    assert remove_empty_strings(["Mike", "", "Emma", "", "Brad"]) == ["Mike", "Emma", "Brad"]
    assert remove_empty_strings([]) == []

def test_add_after_item():
    # add_after_item 테스트
    test_list = [1, 2, 3, 4]
    assert add_after_item(test_list, 2, 2.5) == [1, 2, 2.5, 3, 4]
    
    with pytest.raises(ValueError):
        add_after_item([1, 2, 3], 5, 6)

def test_replace_item():
    # replace_item 테스트
    assert replace_item([5, 10, 15, 20, 25, 50, 20], 20, 200) == [5, 10, 15, 200, 25, 50, 20]
    assert replace_item([5, 10, 15, 20, 25, 50, 20], 20, 200, True) == [5, 10, 15, 200, 25, 50, 200]
    
    with pytest.raises(ValueError):
        replace_item([1, 2, 3], 5, 6)
