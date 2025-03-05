import pytest
from vaildation_data import UserValidator

# UserValidator 테스트
def test_user_validator():
    # validate_username 테스트
    assert UserValidator.validate_username("john_doe123")
    assert not UserValidator.validate_username("jo")  # 너무 짧음
    assert not UserValidator.validate_username("john.doe")  # 허용되지 않는 문자
    
    # validate_email 테스트
    assert UserValidator.validate_email("user@example.com")
    assert not UserValidator.validate_email("invalid-email")
    
    # validate_age 테스트
    assert UserValidator.validate_age(25)
    assert not UserValidator.validate_age("25")  # 문자열, 정수 아님
    assert not UserValidator.validate_age(150)  # 범위 초과
    
    # validate_user 테스트
    valid_user = {
        "username": "john_doe123",
        "email": "john@example.com",
        "age": 30
    }
    assert UserValidator.validate_user(valid_user) == []
    
    invalid_user = {
        "username": "jo",
        "email": "invalid-email",
        "age": 150
    }
    errors = UserValidator.validate_user(invalid_user)
    assert len(errors) == 3