from PIL import Image
import os

# 테스트 이미지 경로
TEST_IMAGE_PATH = "images/test_image.jpg"
OUTPUT_DIR = "images/output"


# Pillow 테스트
from pillow_transformations import (
    load_and_show_image_info, resize_image, crop_image,
    rotate_and_flip_image, apply_filters, convert_image_formats
)

def test_pillow_transformations():
    # 이미지 로드 테스트
    image = load_and_show_image_info(TEST_IMAGE_PATH)
    assert isinstance(image, Image.Image)
    
    # 크기 조정 테스트
    resized = resize_image(image, 200, 150, keep_aspect_ratio=False)
    assert resized.size == (200, 150)
    
    resized_ratio = resize_image(image, 200)
    assert resized_ratio.size[0] == 200
    
    # 자르기 테스트
    cropped = crop_image(image, (50, 50, 150, 150))
    assert cropped.size == (100, 100)
    
    # 회전 및 반전 테스트
    transformed = rotate_and_flip_image(image, 45)
    assert len(transformed) == 3
    
    # 필터 적용 테스트
    filtered = apply_filters(image)
    assert len(filtered) > 0
    
    # 형식 변환 테스트
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    paths = convert_image_formats(image, OUTPUT_DIR)
    assert len(paths) > 0
    for path in paths:
        assert os.path.exists(path)
