from typing import List
def reverse_list(input_list:List)->List:
    """
    리스트의 요소 순서를 뒤집는 함수 (내장 함수 사용하지 않고 구현)
    
    Args:
        input_list (list): 입력 리스트
        
    Returns:
        list: 순서가 뒤집힌 리스트
    """
    # 함수 구현
    return input_list[::-1]
    # return list(reversed(input_list)) 1) 뒤집힌 이터레이터 변환 2) 리스트로 반환

    
def concatenate_lists(list1:List, list2:List)->List:
    """
    두 리스트를 인덱스별로 연결하는 함수
    예: [1,2,3], [4,5,6] -> [1,4,2,5,3,6]
    
    Args:
        list1 (list): 첫 번째 리스트
        list2 (list): 두 번째 리스트
        
    Returns:
        list: 인덱스별로 연결된 리스트
    """
    # 함수 구현                               list1 > list2         list2 > list1
    return list(sum(zip(list1, list2), ())) + list1[len(list2):] + list2[len(list1):]
    
def square_list(numbers:List)->List:
    """
    리스트의 모든 숫자를 제곱하는 함수
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        list: 모든 요소가 제곱된 리스트
    """
    # 함수 구현
    return [num ** 2 for num in numbers]
