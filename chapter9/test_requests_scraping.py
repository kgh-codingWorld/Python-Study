import requests
import os

# Requests 테스트
from requests_scraping import (
    fetch_webpage, fetch_with_params, create_session_with_cookies,
    download_file, fetch_json_api
)

def test_requests_scraping():
    # fetch_webpage 테스트
    html = fetch_webpage("https://httpbin.org/html")
    assert "<html>" in html
    assert "</html>" in html
    
    # fetch_with_params 테스트
    response = fetch_with_params("https://httpbin.org/get", {"param1": "value1", "param2": "value2"})
    assert "param1" in response
    assert "value1" in response
    
    # create_session_with_cookies 테스트
    session = create_session_with_cookies("https://httpbin.org/cookies", {"cookie1": "value1"})
    response = session.get("https://httpbin.org/cookies").text
    assert "cookie1" in response
    assert "value1" in response
    
    # download_file 테스트
    success = download_file("https://httpbin.org/image/jpeg", "test_image.jpg")
    assert success
    assert os.path.exists("test_image.jpg")
    os.remove("test_image.jpg")  # 테스트 후 파일 삭제
    
    # fetch_json_api 테스트
    data = fetch_json_api("https://httpbin.org/json")
    assert "slideshow" in data
