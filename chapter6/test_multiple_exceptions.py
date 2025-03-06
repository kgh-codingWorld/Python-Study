# 다중 예외 처리 테스트
from multiple_exceptions import (
    process_data, convert_to_number, process_file_operations, execute_operations
)

def test_process_data():
    # process_data 테스트
    success, result = process_data(42)
    assert success is True
    
    success, result = process_data("invalid")
    assert success is False

def test_convert_to_number():    
    # convert_to_number 테스트
    assert convert_to_number("42") == 42
    assert convert_to_number("42.5") == 42.5
    assert isinstance(convert_to_number("invalid"), str)

def test_process_file_operations(): 
    # process_file_operations 테스트
    success, result = process_file_operations("test_file.txt", "write", "Test data")
    assert success is True
    
    success, result = process_file_operations("test_file.txt", "read")
    assert success is True
    assert result == "Test data"
    
    success, result = process_file_operations("test_file.txt", "delete")
    assert success is True

def test_execute_operations(): 
    # execute_operations 테스트
    operations = [
        {"type": "math", "operation": "add", "values": [1, 2]},
        {"type": "math", "operation": "divide", "values": [10, 0]},
        {"type": "invalid", "operation": "unknown"}
    ]
    results = execute_operations(operations)
    assert len(results) == 3
    assert results[0]["success"] is True
    assert results[1]["success"] is False
    assert results[2]["success"] is False
