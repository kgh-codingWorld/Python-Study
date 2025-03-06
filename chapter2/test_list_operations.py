from list_operations import reverse_list, concatenate_lists, square_list

# 리스트 기본 연산 테스트
def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list([]) == []

def test_concatenate_lists():
    assert concatenate_lists([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert concatenate_lists([1, 2], [3, 4, 5]) == [1, 3, 2, 4, 5]

def test_square_list():    
    assert square_list([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert square_list([-1, 0, 1]) == [1, 0, 1]