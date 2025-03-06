import scrapy

class NewsArticle(scrapy.Item):
    """뉴스 기사 아이템"""
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    published_date = scrapy.Field()
    content = scrapy.Field()
    
class Product(scrapy.Item):
    """제품 아이템"""
    name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    image_url = scrapy.Field()
    category = scrapy.Field()
