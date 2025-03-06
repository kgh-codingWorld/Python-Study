import cv2
import numpy as np
from typing import Tuple, List, Optional

def load_and_display_image(image_path: str) -> np.ndarray:
    """
    이미지를 로드하고 화면에 표시합니다.
    
    Args:
        image_path: 이미지 파일 경로
        
    Returns:
        로드된 이미지 배열
    """
    # 함수 구현
    
def get_image_properties(image: np.ndarray) -> dict:
    """
    이미지의 속성(크기, 채널 수, 데이터 타입 등)을 반환합니다.
    
    Args:
        image: 이미지 배열
        
    Returns:
        이미지 속성을 담은 딕셔너리
    """
    # 함수 구현
    
def extract_roi(image: np.ndarray, x: int, y: int, width: int, height: int) -> np.ndarray:
    """
    이미지에서 관심 영역(ROI)을 추출합니다.
    
    Args:
        image: 이미지 배열
        x, y: ROI의 시작 좌표
        width, height: ROI의 너비와 높이
        
    Returns:
        추출된 ROI 이미지
    """
    # 함수 구현
    
def split_and_merge_channels(image: np.ndarray) -> Tuple[np.ndarray, List[np.ndarray]]:
    """
    이미지의 색상 채널을 분리하고 다시 병합합니다.
    
    Args:
        image: 이미지 배열
        
    Returns:
        (병합된 이미지, [분리된 채널 리스트])
    """
    # 함수 구현
