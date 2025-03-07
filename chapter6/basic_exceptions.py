from typing import Any, List, Dict, Union, Optional

def safe_division(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """
    안전한 나눗셈 함수 (0으로 나누기 예외 처리)
    
    Args:
        a: 분자
        b: 분모
        
    Returns:
        나눗셈 결과 또는 None (오류 발생 시)
    """
    # 함수 구현
    
def access_list_element(lst: List[Any], index: int) -> Any:
    """
    리스트 요소에 안전하게 접근하는 함수
    
    Args:
        lst: 접근할 리스트
        index: 접근할 인덱스
        
    Returns:
        접근한 요소 또는 None (인덱스 오류 시)
    """
    # 함수 구현
    
def parse_json_data(json_str: str) -> Dict[str, Any]:
    """
    JSON 문자열을 파싱하는 함수
    
    Args:
        json_str: 파싱할 JSON 문자열
        
    Returns:
        파싱된 딕셔너리
        
    Raises:
        ValueError: JSON 형식이 올바르지 않을 경우
    """
    # 함수 구현
    
def read_file_content(file_path: str) -> str:
    """
    파일 내용을 안전하게 읽는 함수
    
    Args:
        file_path: 읽을 파일 경로
        
    Returns:
        파일 내용
        
    Raises:
        FileNotFoundError: 파일을 찾을 수 없을 경우
        PermissionError: 파일 접근 권한이 없을 경우
    """
    # 함수 구현
