import os

# 테스트 이미지 경로
TEST_IMAGE_PATH = "images/test_image.jpg"
OUTPUT_DIR = "images/output"


from image_processing_project import (
    load_image_multiple_libraries, image_enhancement_pipeline,
    edge_detection_comparison, create_image_collage, visualize_processing_steps
    )

def test_image_processing_project():
    # 다중 라이브러리 로드 테스트
    loaded = load_image_multiple_libraries(TEST_IMAGE_PATH)
    assert "opencv" in loaded
    assert "pillow" in loaded
    assert "skimage" in loaded

    # 이미지 향상 파이프라인 테스트
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    enhanced_paths = image_enhancement_pipeline(TEST_IMAGE_PATH, OUTPUT_DIR)
    assert len(enhanced_paths) > 0
    for path in enhanced_paths:
        assert os.path.exists(path)

    # 에지 검출 비교 테스트
    edges = edge_detection_comparison(TEST_IMAGE_PATH)
    assert "canny" in edges
    assert "sobel" in edges
    assert "prewitt" in edges

    # 콜라주 생성 테스트
    image_paths = [TEST_IMAGE_PATH] * 4  # 같은 이미지 4개 사용
    collage_path = os.path.join(OUTPUT_DIR, "collage.jpg")
    result_path = create_image_collage(image_paths, collage_path, (2, 2))
    assert os.path.exists(result_path)

    # 처리 단계 시각화 테스트
    visualize_processing_steps(TEST_IMAGE_PATH)
