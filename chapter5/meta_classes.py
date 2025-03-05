from typing import Type, Dict, Any, Callable
from functools import wraps

def singleton(cls: Type) -> Callable:
    """
    클래스를 싱글톤으로 만드는 데코레이터
    
    Args:
        cls: 싱글톤으로 만들 클래스
        
    Returns:
        싱글톤 패턴이 적용된 클래스
    """
    # 데코레이터 구현
    
class LoggingMeta(type):
    """
    모든 메서드 호출을 로깅하는 메타클래스
    """
    
    def __new__(mcs, name: str, bases: tuple, namespace: Dict[str, Any]):
        """
        클래스 생성 시 모든 메서드에 로깅 기능 추가
        
        Args:
            name: 클래스 이름
            bases: 기본 클래스 튜플
            namespace: 클래스 네임스페이스
            
        Returns:
            로깅 기능이 추가된 클래스
        """
        # 메서드 구현
        
    @staticmethod
    def add_logging(method: Callable) -> Callable:
        """
        메서드에 로깅 기능을 추가하는 함수
        
        Args:
            method: 로깅을 추가할 메서드
            
        Returns:
            로깅 기능이 추가된 메서드
        """
        # 메서드 구현
