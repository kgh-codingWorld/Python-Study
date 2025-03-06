from typing import Union

# Union : 여러 개의 자료형을 가질 수 있는 타입 힌트 도구
# add라는 이름의 함수 정의
# a와 b는 각각 int 또는 float을 받을 수 있음      반환값 : int 또는 float으로 받을 수 있음
def add(a:Union[int,float], b:Union[int,float])->Union[int,float]:
    """
    두 숫자를 더하는 함수
    
    Args:
        a (int/float): 첫 번째 숫자
        b (int/float): 두 번째 숫자
        
    Returns:
        int/float: 두 숫자의 합
    """
    # 함수 구현
    return a + b
    
    
def subtract(a:Union[int,float], b:Union[int,float])->Union[int,float]:
    """
    첫 번째 숫자에서 두 번째 숫자를 빼는 함수
    
    Args:
        a (int/float): 첫 번째 숫자
        b (int/float): 두 번째 숫자
        
    Returns:
        int/float: 뺄셈 결과
    """
    # 함수 구현
    return a - b
    
def multiply(a:Union[int,float], b:Union[int,float])->Union[int,float]:
    """
    두 숫자를 곱하는 함수
    
    Args:
        a (int/float): 첫 번째 숫자
        b (int/float): 두 번째 숫자
        
    Returns:
        int/float: 곱셈 결과
    """
    # 함수 구현
    return a * b
    
def divide(a:Union[int,float], b:Union[int,float])->Union[int,float]:
    """
    첫 번째 숫자를 두 번째 숫자로 나누는 함수
    
    Args:
        a (int/float): 첫 번째 숫자
        b (int/float): 두 번째 숫자
        
    Returns:
        float: 나눗셈 결과
        
    Raises:
        ZeroDivisionError: b가 0일 경우 발생
    """
    # 함수 구현
    if b==0 :
        ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b
    
def power(a:Union[int,float], b:Union[int,float])->Union[int,float]:
    """
    첫 번째 숫자를 두 번째 숫자만큼 제곱하는 함수
    
    Args:
        a (int/float): 밑
        b (int/float): 지수
        
    Returns:
        int/float: 거듭제곱 결과
    """
    # 함수 구현
    return a ** b
