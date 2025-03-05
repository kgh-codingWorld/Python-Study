from typing import TypeVar, Generic, List, Dict, Any, Callable, Optional, Union

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class DataProcessor(Generic[T]):
    """
    데이터 처리를 위한 제네릭 클래스
    
    Attributes:
        data: 처리할 데이터
        validators: 데이터 검증을 위한 함수 리스트
    """
    
    def __init__(self, data: T, validators: Optional[List[Callable[[T], bool]]] = None):
        """
        DataProcessor 클래스의 생성자
        
        Args:
            data: 처리할 데이터
            validators: 데이터 검증을 위한 함수 리스트
            
        Raises:
            ValueError: 데이터가 유효하지 않을 경우
        """
        # 속성 초기화 구현
    
    def map(self, mapper: Callable[[T], V]) -> 'DataProcessor[V]':
        """
        데이터를 변환하는 함수
        
        Args:
            mapper: 데이터를 변환하는 함수
            
        Returns:
            변환된 데이터를 가진 새 DataProcessor 인스턴스
        """
        # 메서드 구현
    
    def filter(self, predicate: Callable[[T], bool]) -> 'DataProcessor[T]':
        """
        조건에 맞는 데이터만 필터링하는 함수
        
        Args:
            predicate: 필터링 조건 함수
            
        Returns:
            필터링된 데이터를 가진 새 DataProcessor 인스턴스
        """
        # 메서드 구현
    
    def get_data(self) -> T:
        """
        처리된 데이터를 반환
        
        Returns:
            처리된 데이터
        """
        # 메서드 구현


class ListProcessor(DataProcessor[List[T]]):
    """
    리스트 데이터 처리를 위한 특화된 클래스
    """
    
    def group_by(self, key_func: Callable[[T], K]) -> Dict[K, List[T]]:
        """
        리스트 항목을 지정된 키 함수에 따라 그룹화하는 함수
        
        Args:
            key_func: 각 항목에서 그룹화 키를 추출하는 함수
            
        Returns:
            키별로 그룹화된 딕셔너리
        """
        # 메서드 구현
    
    def sort_by(self, key_func: Callable[[T], Any], reverse: bool = False) -> 'ListProcessor[T]':
        """
        리스트를 지정된 키 함수에 따라 정렬하는 함수
        
        Args:
            key_func: 정렬 키를 추출하는 함수
            reverse: 역순 정렬 여부
            
        Returns:
            정렬된 데이터를 가진 새 ListProcessor 인스턴스
        """
        # 메서드 구현
