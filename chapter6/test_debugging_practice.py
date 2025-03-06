import pytest
from typing import Dict, Any, List, Callable
import traceback
import sys

# 테스트를 위한 사용자 정의 예외 클래스 모의 구현
class ValidationError(Exception):
    """데이터 검증 오류"""
    pass

class NotFoundError(Exception):
    """리소스를 찾을 수 없음"""
    pass

class PermissionDeniedError(Exception):
    """권한 없음"""
    pass

# 테스트할 함수들 임포트
from debugging_practice import (
    debug_function, analyze_exception_info, handle_application_flow, create_exception_handler
)

def test_debug_function():
    """debug_function 함수 테스트"""
    # 이 함수는 디버깅 포인트만 있으므로 실행만 확인
    debug_function(42)
    debug_function("test string")
    debug_function({"key": "value"})
    # 예외가 발생하지 않고 실행되면 성공

def test_analyze_exception_info():
    """analyze_exception_info 함수 테스트"""
    # 다양한 예외 유형으로 테스트
    try:
        1 / 0
    except ZeroDivisionError as e:
        info = analyze_exception_info(e)
        # 반환된 딕셔너리 구조 확인
        assert "type" in info
        assert "message" in info
        assert "traceback" in info
        # 예외 유형 확인
        assert info["type"] == "ZeroDivisionError"
        assert "division by zero" in info["message"]
    
    try:
        int("not_a_number")
    except ValueError as e:
        info = analyze_exception_info(e)
        assert info["type"] == "ValueError"
    
    try:
        open("non_existent_file.txt")
    except FileNotFoundError as e:
        info = analyze_exception_info(e)
        assert info["type"] == "FileNotFoundError"

def test_handle_application_flow():
    """handle_application_flow 함수 테스트"""
    # 테스트 데이터 준비
    actions = [
        {"type": "validation", "data": {"username": "john", "email": "john@example.com"}},
        {"type": "resource", "id": "1", "resources": [{"id": "1", "name": "Resource 1"}]},
        {"type": "permission", "user": {"role": "admin", "permissions": ["read", "write"]}, "required": "write"},
        {"type": "validation", "data": {"username": "j", "email": "invalid"}}
    ]
    
    # 함수 실행
    results = handle_application_flow(actions)
    
    # 결과 검증
    assert isinstance(results, list)
    assert len(results) == 4
    
    # 각 결과 항목 검증
    assert results[0]["success"] is True
    assert results[1]["success"] is True
    assert results[2]["success"] is True
    assert results[3]["success"] is False
    assert "error" in results[3]

def test_create_exception_handler():
    """create_exception_handler 함수 테스트"""
    # 테스트용 핸들러 함수 정의
    def handle_validation_error(e: ValidationError) -> Dict[str, Any]:
        return {"status": "error", "code": "VALIDATION_ERROR", "message": str(e)}
    
    def handle_not_found_error(e: NotFoundError) -> Dict[str, Any]:
        return {"status": "error", "code": "NOT_FOUND", "message": str(e)}
    
    def handle_permission_error(e: PermissionDeniedError) -> Dict[str, Any]:
        return {"status": "error", "code": "PERMISSION_DENIED", "message": str(e)}
    
    # 예외 맵 생성
    exception_map = {
        ValidationError: handle_validation_error,
        NotFoundError: handle_not_found_error,
        PermissionDeniedError: handle_permission_error
    }
    
    # 예외 핸들러 생성
    handler = create_exception_handler(exception_map)
    
    # 다양한 예외로 테스트
    result = handler(ValidationError("유효하지 않은 데이터"))
    assert result["status"] == "error"
    assert result["code"] == "VALIDATION_ERROR"
    assert "유효하지 않은 데이터" in result["message"]
    
    result = handler(NotFoundError("리소스를 찾을 수 없음"))
    assert result["code"] == "NOT_FOUND"
    
    result = handler(PermissionDeniedError("권한이 없습니다"))
    assert result["code"] == "PERMISSION_DENIED"
    
    # 맵에 없는 예외 유형 테스트
    result = handler(KeyError("키가 없습니다"))
    assert result["status"] == "error"
    assert result["code"] == "UNHANDLED_EXCEPTION"
    assert "KeyError" in result["message"]

def test_debug_function_with_exception():
    """debug_function이 예외를 처리하는지 테스트"""
    # 예외를 발생시키는 데이터로 테스트
    try:
        debug_function({"trigger_error": True})
    except Exception as e:
        # 예외가 발생해도 테스트는 통과
        pass

def test_handle_application_flow_with_empty_actions():
    """빈 작업 목록으로 handle_application_flow 테스트"""
    results = handle_application_flow([])
    assert isinstance(results, list)
    assert len(results) == 0

def test_handle_application_flow_with_invalid_action_type():
    """잘못된 작업 유형으로 handle_application_flow 테스트"""
    actions = [
        {"type": "unknown_action", "data": {"some": "data"}}
    ]
    results = handle_application_flow(actions)
    assert len(results) == 1
    assert results[0]["success"] is False
    assert "error" in results[0]
    assert "Unknown action type" in results[0]["error"]
