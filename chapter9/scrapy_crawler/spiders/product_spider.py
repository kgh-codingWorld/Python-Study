import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_crawler.items import Product

class ProductSpider(CrawlSpider):
    """제품 카탈로그 크롤링을 위한 스파이더"""
    name = "products"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/products"]
    
    rules = (
        # 제품 페이지 규칙
        Rule(LinkExtractor(allow=r'items/\d+'), callback='parse_item'),
        # 카테고리 페이지 규칙
        Rule(LinkExtractor(allow=r'category/'), follow=True),
    )
    
    def parse_item(self, response):
        """제품 상세 페이지 파싱"""
        # 스파이더 구현
