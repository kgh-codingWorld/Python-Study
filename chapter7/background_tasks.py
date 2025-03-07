import asyncio
import logging
from typing import Dict, Any, List
from datetime import datetime

# 로거 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def send_welcome_email(user_data: Dict[str, Any]):
    """
    사용자 가입 환영 이메일을 전송하는 백그라운드 태스크
    
    Args:
        user_data: 사용자 정보
    """
    # 이메일 전송 지연 시뮬레이션
    await asyncio.sleep(2)
    logger.info(f"환영 이메일 전송 완료: {user_data['email']}, 사용자명: {user_data['username']}")

async def process_product_data(product_data: Dict[str, Any]):
    """
    제품 데이터를 처리하는 백그라운드 태스크
    
    Args:
        product_data: 제품 정보
    """
    # 데이터 처리 지연 시뮬레이션
    await asyncio.sleep(3)
    logger.info(f"제품 데이터 처리 완료: {product_data['name']}, ID: {product_data['id']}")

async def generate_reports(date: datetime, report_type: str):
    """
    보고서를 생성하는 백그라운드 태스크
    
    Args:
        date: 보고서 날짜
        report_type: 보고서 유형
    """
    # 보고서 생성 지연 시뮬레이션
    await asyncio.sleep(5)
    logger.info(f"{report_type} 보고서 생성 완료: {date.strftime('%Y-%m-%d')}")

async def batch_process_items(items: List[Dict[str, Any]]):
    """
    여러 아이템을 일괄 처리하는 백그라운드 태스크
    
    Args:
        items: 처리할 아이템 목록
    """
    # 일괄 처리 지연 시뮬레이션
    await asyncio.sleep(1)
    for item in items:
        await asyncio.sleep(0.5)
        logger.info(f"아이템 처리 완료: {item['name']}")
    logger.info(f"총 {len(items)}개 아이템 일괄 처리 완료")
