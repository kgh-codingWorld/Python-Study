import time
from decorators import timing_decorator, retry, memoize


# 데코레이터 테스트
def test_timing_decorator():
    # timing_decorator 테스트
    @timing_decorator
    def slow_function(n):
        time.sleep(0.1)
        return n * 2
    
    result = slow_function(5)
    assert result == 10

def test_retry():
    # retry 데코레이터 테스트
    attempt_count = 0
    
    @retry(max_attempts=3, delay=0.1)
    def failing_function():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ValueError("일시적인 오류")
        return "성공"
    
    result = failing_function()
    assert result == "성공"
    assert attempt_count == 3

def test_memoize():
    # memoize 데코레이터 테스트
    call_count = 0
    
    @memoize
    def fibonacci(n):
        nonlocal call_count
        call_count += 1
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    assert fibonacci(10) == 55
    # 메모이제이션이 없으면 fibonacci(10)은 177번 호출됨
    # 메모이제이션이 있으면 11번만 호출됨
    assert call_count <= 11
