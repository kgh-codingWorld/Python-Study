from typing import List,Union

def find_max(numbers:List)->Union[int,float]:
    """
    숫자 리스트에서 최댓값을 찾는 함수
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        int/float: 최댓값
        
    Raises:
        ValueError: 리스트가 비어있을 경우
    """
    # 함수 구현
    if not numbers:
        ValueError("리스트가 비어있습니다.")
    return max(numbers)
    
def filter_even_numbers(numbers:List)->List:
    """
    리스트에서 짝수만 필터링하는 함수
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        list: 짝수만 포함된 리스트
    """
    # 함수 구현
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
    
def average(numbers:List)->float:
    """
    숫자 리스트의 평균을 계산하는 함수
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        float: 평균값
        
    Raises:
        ValueError: 리스트가 비어있을 경우
    """
    # 함수 구현
    if not numbers:
        return ValueError("리스트가 비어있습니다.")
    return sum(numbers) / len(numbers)
