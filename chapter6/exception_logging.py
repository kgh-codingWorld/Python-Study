import logging
from typing import Any, Dict, List, Optional, Callable, Tuple
import traceback
import sys

def setup_logger(log_file: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """
    로거를 설정하는 함수
    
    Args:
        log_file: 로그 파일 경로 (None이면 콘솔에만 출력)
        level: 로깅 레벨
        
    Returns:
        설정된 로거
    """
    # 함수 구현
    
def log_exception(logger: logging.Logger, exception: Exception, 
                additional_info: Optional[Dict[str, Any]] = None) -> None:
    """
    예외를 로깅하는 함수
    
    Args:
        logger: 로거 객체
        exception: 로깅할 예외
        additional_info: 추가 정보 (선택 사항)
    """
    # 함수 구현
    
def safe_execute(func: Callable, *args, **kwargs) -> Tuple[bool, Any, Optional[str]]:
    """
    함수를 안전하게 실행하고 예외를 로깅하는 함수
    
    Args:
        func: 실행할 함수
        *args: 함수에 전달할 위치 인자
        **kwargs: 함수에 전달할 키워드 인자
        
    Returns:
        (성공 여부, 결과 또는 None, 오류 메시지 또는 None)
    """
    # 함수 구현
    
def retry_operation(func: Callable, max_attempts: int = 3, 
                  retry_exceptions: Optional[List[type]] = None, 
                  logger: Optional[logging.Logger] = None) -> Callable:
    """
    작업을 재시도하는 데코레이터 함수
    
    Args:
        func: 재시도할 함수
        max_attempts: 최대 시도 횟수
        retry_exceptions: 재시도할 예외 유형 목록
        logger: 로거 객체
        
    Returns:
        래핑된 함수
    """
    # 함수 구현
