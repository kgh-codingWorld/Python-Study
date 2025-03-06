import pytest

# 사용자 정의 예외 테스트
from custom_exceptions import (
    ValidationError, NotFoundError, PermissionDeniedError, RateLimitExceededError,
    validate_user_data, find_resource, check_permission, make_api_request
)

def test_validate_user_data():
    # validate_user_data 테스트
    valid_user = {
        "username": "john_doe",
        "email": "john@example.com",
        "age": 30
    }
    validate_user_data(valid_user)  # 예외가 발생하지 않아야 함
    
    invalid_user = {
        "username": "j",  # 너무 짧음
        "email": "invalid-email",
        "age": -5  # 음수
    }
    with pytest.raises(ValidationError):
        validate_user_data(invalid_user)

def test_find_resource():   
    # find_resource 테스트
    resources = [
        {"id": "1", "name": "Resource 1"},
        {"id": "2", "name": "Resource 2"}
    ]
    assert find_resource("2", resources) == {"id": "2", "name": "Resource 2"}
    
    with pytest.raises(NotFoundError):
        find_resource("3", resources)

def test_check_permission():    
    # check_permission 테스트
    admin_user = {"role": "admin", "permissions": ["read", "write", "delete"]}
    check_permission(admin_user, "write")  # 예외가 발생하지 않아야 함
    
    guest_user = {"role": "guest", "permissions": ["read"]}
    with pytest.raises(PermissionDeniedError):
        check_permission(guest_user, "write")

def test_make_api_request():
    # make_api_request 테스트
    assert isinstance(make_api_request("valid_key", 5), dict)
    
    with pytest.raises(RateLimitExceededError):
        make_api_request("valid_key", 15)
