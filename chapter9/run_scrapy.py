from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_crawler.spiders.news_spider import NewsSpider
from scrapy_crawler.spiders.product_spider import ProductSpider

def run_spider(spider_name: str, output_file: str = None):
    """
    Scrapy 스파이더를 실행합니다.
    
    Args:
        spider_name: 실행할 스파이더 이름
        output_file: 출력 파일 경로 (기본값: None)
    """
    # 함수 구현

if __name__ == "__main__":
    # 스파이더 실행 코드
    pass
