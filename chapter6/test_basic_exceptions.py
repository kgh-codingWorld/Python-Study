import os,pytest

# 기본 예외 처리 테스트
from basic_exceptions import (
    safe_division, access_list_element, parse_json_data, read_file_content
)

def test_safe_division():
    # safe_division 테스트
    assert safe_division(10, 2) == 5.0
    assert safe_division(10, 0) is None

def test_access_list_element():
    # access_list_element 테스트
    test_list = [1, 2, 3, 4, 5]
    assert access_list_element(test_list, 2) == 3
    assert access_list_element(test_list, 10) is None

def test_parse_json_data():  
    # parse_json_data 테스트
    valid_json = '{"name": "John", "age": 30}'
    assert parse_json_data(valid_json) == {"name": "John", "age": 30}
    
    invalid_json = '{name: John, age: 30}'
    with pytest.raises(ValueError):
        parse_json_data(invalid_json)

def test_read_file_content():
    # read_file_content 테스트
    # 테스트 파일 생성
    with open("test_file.txt", "w") as f:
        f.write("Hello, World!")
    
    assert read_file_content("test_file.txt") == "Hello, World!"
    
    with pytest.raises(FileNotFoundError):
        read_file_content("non_existent_file.txt")
    
    # 테스트 파일 삭제
    os.remove("test_file.txt")
