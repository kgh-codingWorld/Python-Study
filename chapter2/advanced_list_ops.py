from typing import List,Callable,Optional,Any

def custom_map(function:Callable, input_list:List)->List:
    """
    내장 map 함수를 사용하지 않고 리스트의 모든 요소에 함수를 적용하는 함수
    
    Args:
        function: 각 요소에 적용할 함수
        input_list (list): 입력 리스트
        
    Returns:
        list: 함수가 적용된 결과 리스트
    """
    # 함수 구현
    return [function(item) for item in input_list]
    
def custom_filter(predicate:Callable, input_list:List)->List:
    """
    내장 filter 함수를 사용하지 않고 조건에 맞는 요소만 필터링하는 함수
    
    Args:
        predicate: 각 요소를 평가하는 함수 (True/False 반환)
        input_list (list): 입력 리스트
        
    Returns:
        list: 조건에 맞는 요소만 포함된 리스트
    """
    # 함수 구현
    return [item for item in input_list if predicate(item)]
    
def custom_reduce(function:Callable, input_list:List, initial:Optional[Any]=None)->Any:
    """
    내장 reduce 함수를 사용하지 않고 리스트의 요소를 누적 계산하는 함수
    
    Args:
        function: 두 인자를 받아 하나의 값을 반환하는 함수
        input_list (list): 입력 리스트
        initial: 초기값 (기본값: None)
        
    Returns:
        결과값
        
    Raises:
        ValueError: 리스트가 비어있고 초기값이 None일 경우
    """
    # 함수 구현
    if not input_list and initial is None:
        raise ValueError("list is empty")
    
    # iter : 반복자
    it = iter(input_list)
    result = initial if initial is not None else next(it) # 초기값 x > 첫 번째 요소를 초기값으로 사용용

    for item in it:
        result = function(result, item) # 누적 연산 수행
    return result

