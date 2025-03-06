from fastapi.testclient import TestClient
import pytest
from main import app
from advanced_models import UserRole, ProductCategory

# 테스트 클라이언트 생성
client = TestClient(app)

# 루트 경로 테스트
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

# 상태 확인 테스트
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

# 사용자 생성 테스트
def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "securepassword123",
        "role": UserRole.USER
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
    assert "id" in data
    assert "password" not in data  # 비밀번호는 응답에 포함되지 않아야 함

# 제품 생성 테스트 (인증 필요)
def test_create_product():
    # 먼저 관리자 사용자 생성 및 로그인 필요
    # 이 부분은 실제 구현에 따라 달라질 수 있음
    
    product_data = {
        "id": 1,
        "name": "Test Product",
        "description": "This is a test product",
        "price": 99.99,
        "category": ProductCategory.ELECTRONICS,
        "in_stock": True,
        "tags": ["test", "sample"]
    }
    
    # 인증 토큰 없이 요청 (실패해야 함)
    response = client.post("/products/", json=product_data)
    assert response.status_code == 401
    
    # 실제 테스트에서는 인증 토큰을 포함하여 요청
    # headers = {"Authorization": f"Bearer {token}"}
    # response = client.post("/products/", json=product_data, headers=headers)
    # assert response.status_code == 201
