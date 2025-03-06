import logging

# 예외 처리와 로깅 테스트
from exception_logging import (
    setup_logger, log_exception, safe_execute, retry_operation
)

def test_exception_logging():
    # setup_logger 테스트
    logger = setup_logger()
    assert isinstance(logger, logging.Logger)
    
    # log_exception 테스트
    try:
        1 / 0
    except Exception as e:
        log_exception(logger, e, {"context": "테스트"})
    
    # safe_execute 테스트
    def successful_function():
        return 42
    
    def failing_function():
        raise ValueError("테스트 오류")
    
    success, result, error = safe_execute(successful_function)
    assert success is True
    assert result == 42
    assert error is None
    
    success, result, error = safe_execute(failing_function)
    assert success is False
    assert result is None
    assert "테스트 오류" in error
    
    # retry_operation 테스트
    call_count = 0
    
    @retry_operation(max_attempts=3)
    def temporary_failing_function():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ConnectionError("일시적 오류")
        return "성공"
    
    result = temporary_failing_function()
    assert result == "성공"
    assert call_count == 3
