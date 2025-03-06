from PIL import Image, ImageFilter
from typing import Tuple, Optional, List
import numpy as np

def load_and_show_image_info(image_path: str) -> Image.Image:
    """
    이미지를 로드하고 정보를 출력합니다.
    
    Args:
        image_path: 이미지 파일 경로
        
    Returns:
        로드된 PIL 이미지 객체
    """
    # 함수 구현
    
def resize_image(image: Image.Image, width: int, height: Optional[int] = None, 
                keep_aspect_ratio: bool = True) -> Image.Image:
    """
    이미지 크기를 조정합니다.
    
    Args:
        image: PIL 이미지 객체
        width: 새 너비
        height: 새 높이 (None이면 비율에 맞게 계산)
        keep_aspect_ratio: 가로세로 비율 유지 여부
        
    Returns:
        크기가 조정된 이미지
    """
    # 함수 구현
    
def crop_image(image: Image.Image, box: Tuple[int, int, int, int]) -> Image.Image:
    """
    이미지를 자릅니다.
    
    Args:
        image: PIL 이미지 객체
        box: 자를 영역 (left, upper, right, lower)
        
    Returns:
        잘린 이미지
    """
    # 함수 구현
    
def rotate_and_flip_image(image: Image.Image, angle: float) -> List[Image.Image]:
    """
    이미지를 회전하고 좌우/상하 반전합니다.
    
    Args:
        image: PIL 이미지 객체
        angle: 회전 각도
        
    Returns:
        [회전된 이미지, 좌우 반전 이미지, 상하 반전 이미지]
    """
    # 함수 구현
    
def apply_filters(image: Image.Image) -> List[Image.Image]:
    """
    다양한 필터를 이미지에 적용합니다.
    
    Args:
        image: PIL 이미지 객체
        
    Returns:
        필터가 적용된 이미지 리스트
    """
    # 함수 구현
    
def convert_image_formats(image: Image.Image, output_dir: str) -> List[str]:
    """
    이미지를 다양한 형식으로 저장합니다.
    
    Args:
        image: PIL 이미지 객체
        output_dir: 출력 디렉토리
        
    Returns:
        저장된 파일 경로 리스트
    """
    # 함수 구현
