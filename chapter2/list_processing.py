from typing import List,Any

def remove_empty_strings(string_list:List[str])->List[str]:
    """
    문자열 리스트에서 빈 문자열을 제거하는 함수
    
    Args:
        string_list (list): 문자열 리스트
        
    Returns:
        list: 빈 문자열이 제거된 리스트
    """
    # 함수 구현
    return [s for s in string_list if s != ""]
    
def add_after_item(input_list:List, target_item:Any, new_item:Any)->List[Any]:
    """
    리스트에서 특정 항목 뒤에 새 항목을 추가하는 함수
    
    Args:
        input_list (list): 입력 리스트
        target_item: 찾을 항목
        new_item: 추가할 새 항목
        
    Returns:
        list: 항목이 추가된 리스트
        
    Raises:
        ValueError: target_item이 리스트에 없을 경우
    """
    # 함수 구현
    # 그냥 not target_item은 target_item이 0, False, None일 때도 예외를 발생
    if not target_item in input_list:    
        raise ValueError("target_item is empty")
    return [x for item in input_list for x in ([item, new_item] if item == target_item else [item])]
    
def replace_item(input_list:List[Any], old_item:Any, new_item:Any, replace_all:bool=False)->List[Any]:
    """
    리스트에서 특정 항목을 새 항목으로 교체하는 함수
    
    Args:
        input_list (list): 입력 리스트
        old_item: 교체할 항목
        new_item: 새 항목
        replace_all (bool): True면 모든 항목 교체, False면 첫 번째 항목만 교체
        
    Returns:
        list: 항목이 교체된 리스트
        
    Raises:
        ValueError: old_item이 리스트에 없을 경우
    """
    # 함수 구현
    if not old_item in input_list:
        raise ValueError("old_item is empty")
    if replace_all:
        # true
        return [new_item if item == old_item else item for item in input_list]
    
    # false
    result = input_list[:]
    for i, item in enumerate(result):
        if item == old_item:
            result[i] = new_item
            break
    return result
