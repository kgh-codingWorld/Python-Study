# test_chapter9.py
import numpy as np

# 테스트 이미지 경로
TEST_IMAGE_PATH = "images/test_image.jpg"
OUTPUT_DIR = "images/output"

# OpenCV 테스트
from opencv_basics import (
    load_and_display_image, get_image_properties, 
    extract_roi, split_and_merge_channels
)

def test_opencv_basics():
    # 이미지 로드 테스트
    image = load_and_display_image(TEST_IMAGE_PATH)
    assert image is not None
    assert isinstance(image, np.ndarray)
    
    # 이미지 속성 테스트
    props = get_image_properties(image)
    assert "height" in props
    assert "width" in props
    assert "channels" in props
    assert "dtype" in props
    
    # ROI 추출 테스트
    roi = extract_roi(image, 50, 50, 100, 100)
    assert roi.shape[0] == 100
    assert roi.shape[1] == 100
    
    # 채널 분리 및 병합 테스트
    merged, channels = split_and_merge_channels(image)
    assert len(channels) == 3
    assert merged.shape == image.shape