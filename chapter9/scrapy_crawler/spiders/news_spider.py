import scrapy
from scrapy_crawler.items import NewsArticle

class NewsSpider(scrapy.Spider):
    """뉴스 웹사이트 크롤링을 위한 스파이더"""
    name = "news"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/news"]
    
    def parse(self, response):
        """뉴스 목록 페이지 파싱"""
        # 스파이더 구현
        
    def parse_article(self, response):
        """개별 뉴스 기사 파싱"""
        # 스파이더 구현
