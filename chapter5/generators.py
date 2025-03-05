from typing import Iterator, List, TypeVar, Generator

T = TypeVar('T')

def fibonacci_generator(n: int) -> Iterator[int]:
    """
    피보나치 수열을 생성하는 제너레이터
    
    Args:
        n: 생성할 피보나치 수열의 길이
        
    Yields:
        피보나치 수열의 다음 숫자
    """
    # 함수 구현
    
def chunk_iterator(data: List[T], chunk_size: int) -> Generator[List[T], None, None]:
    """
    리스트를 지정된 크기의 청크로 나누는 제너레이터
    
    Args:
        data: 청크로 나눌 리스트
        chunk_size: 각 청크의 크기
        
    Yields:
        지정된 크기의 청크 리스트
    """
    # 함수 구현
    
def infinite_sequence() -> Generator[int, None, None]:
    """
    무한 시퀀스를 생성하는 제너레이터
    
    Yields:
        순차적으로 증가하는 정수
    """
    # 함수 구현
