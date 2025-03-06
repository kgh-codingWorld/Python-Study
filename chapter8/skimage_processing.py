import numpy as np

# 테스트 이미지 경로
TEST_IMAGE_PATH = "chapter6/images/test_image.jpg"
OUTPUT_DIR = "chapter6/images/output"

# scikit-image 테스트
from skimage_processing import (
    load_and_convert_to_grayscale, resize_skimage,
    apply_threshold, extract_image_region, apply_multiple_filters
)

def test_skimage_processing():
    # 이미지 로드 및 변환 테스트
    original, gray = load_and_convert_to_grayscale(TEST_IMAGE_PATH)
    assert original.ndim == 3
    assert gray.ndim == 2
    
    # 크기 조정 테스트
    resized = resize_skimage(original, (200, 200))
    assert resized.shape[:2] == (200, 200)
    
    # 임계값 처리 테스트
    binary = apply_threshold(gray, 0.5)
    assert np.array_equal(np.unique(binary), np.array([0, 1]))
    
    # 영역 추출 테스트
    region = extract_image_region(original, 50, 150, 50, 150)
    assert region.shape[:2] == (100, 100)
    
    # 필터 적용 테스트
    filtered_images = apply_multiple_filters(gray)
    assert len(filtered_images) > 0