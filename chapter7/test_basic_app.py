import requests
import json
import pytest

# 테스트 서버 URL
BASE_URL = "http://localhost:8000"

def test_root():
    """루트 경로 테스트"""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "안녕하세요! FastAPI에 오신 것을 환영합니다!"

def test_create_item():
    """아이템 생성 테스트"""
    item_data = {
        "name": "테스트 아이템",
        "price": 99.99,
        "is_offer": True,
        "tags": ["테스트", "샘플"],
        "description": "이것은 테스트 아이템입니다."
    }
    
    response = requests.post(f"{BASE_URL}/items/", json=item_data)
    assert response.status_code == 201
    created_item = response.json()
    
    assert created_item["name"] == item_data["name"]
    assert created_item["price"] == item_data["price"]
    assert created_item["is_offer"] == item_data["is_offer"]
    assert created_item["tags"] == item_data["tags"]
    assert created_item["description"] == item_data["description"]
    
    # 생성된 아이템의 ID 저장 (다음 테스트에서 사용)
    return created_item

def test_read_items():
    """아이템 목록 조회 테스트"""
    response = requests.get(f"{BASE_URL}/items/")
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)
    
    # 페이지네이션 테스트
    response = requests.get(f"{BASE_URL}/items/?skip=0&limit=5")
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)
    assert len(items) <= 5

def test_read_item(created_item):
    """특정 아이템 조회 테스트"""
    item_id = created_item["id"]
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    assert response.status_code == 200
    item = response.json()
    assert item["name"] == created_item["name"]
    assert item["price"] == created_item["price"]
    
    # 존재하지 않는 아이템 조회 테스트
    response = requests.get(f"{BASE_URL}/items/9999")
    assert response.status_code == 404

def test_update_item(created_item):
    """아이템 업데이트 테스트"""
    item_id = created_item["id"]
    updated_data = {
        "name": "업데이트된 아이템",
        "price": 199.99,
        "is_offer": False,
        "tags": ["업데이트", "테스트"],
        "description": "이 아이템은 업데이트되었습니다."
    }
    
    response = requests.put(f"{BASE_URL}/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    updated_item = response.json()
    
    assert updated_item["name"] == updated_data["name"]
    assert updated_item["price"] == updated_data["price"]
    assert updated_item["is_offer"] == updated_data["is_offer"]
    
    # 존재하지 않는 아이템 업데이트 테스트
    response = requests.put(f"{BASE_URL}/items/9999", json=updated_data)
    assert response.status_code == 404

def test_delete_item(created_item):
    """아이템 삭제 테스트"""
    item_id = created_item["id"]
    response = requests.delete(f"{BASE_URL}/items/{item_id}")
    assert response.status_code == 200
    
    # 삭제된 아이템 조회 테스트
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    assert response.status_code == 404
    
    # 존재하지 않는 아이템 삭제 테스트
    response = requests.delete(f"{BASE_URL}/items/9999")
    assert response.status_code == 404

def test_validation():
    """입력 데이터 검증 테스트"""
    # 유효하지 않은 아이템 데이터 (가격이 음수)
    invalid_item = {
        "name": "유효하지 않은 아이템",
        "price": -10.0,
        "is_offer": True
    }
    
    response = requests.post(f"{BASE_URL}/items/", json=invalid_item)
    assert response.status_code == 422  # Unprocessable Entity
    
    # 유효하지 않은 아이템 데이터 (이름이 너무 김)
    invalid_item = {
        "name": "a" * 51,  # 51자 (최대 50자)
        "price": 10.0,
        "is_offer": True
    }
    
    response = requests.post(f"{BASE_URL}/items/", json=invalid_item)
    assert response.status_code == 422

# pytest 픽스처를 사용하여 테스트 간에 생성된 아이템 공유
@pytest.fixture(scope="module")
def created_item():
    """테스트에서 사용할 아이템 생성"""
    return test_create_item()

if __name__ == "__main__":
    # 개별 실행을 위한 코드
    print("테스트 시작...")
    
    # 테스트 실행
    test_root()
    item = test_create_item()
    test_read_items()
    test_read_item(item)
    test_update_item(item)
    test_delete_item(item)
    test_validation()
    
    print("모든 테스트 완료!")
