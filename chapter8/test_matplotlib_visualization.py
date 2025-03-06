import matplotlib.pyplot as plt

# 테스트 이미지 경로
TEST_IMAGE_PATH = "images/test_image.jpg"
OUTPUT_DIR = "images/output"


# Matplotlib 테스트
from matplotlib_visualization import (
    display_image_with_matplotlib, visualize_rgb_channels,
    display_grayscale_image, plot_image_histogram, create_image_grid
)

def test_matplotlib_visualization():
    # 이미지 표시 테스트
    display_image_with_matplotlib(TEST_IMAGE_PATH, "Test Image")
    
    # 이미지 로드
    image = plt.imread(TEST_IMAGE_PATH)
    
    # RGB 채널 시각화 테스트
    visualize_rgb_channels(image)
    
    # 그레이스케일 변환 테스트
    gray_image = display_grayscale_image(image)
    assert gray_image.ndim == 2
    
    # 히스토그램 테스트
    plot_image_histogram(image)
    
    # 이미지 그리드 테스트
    images = [image, gray_image, gray_image]
    titles = ["Original", "Grayscale", "Grayscale Copy"]
    create_image_grid(images, titles)
