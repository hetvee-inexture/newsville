import scrapy
from news_scraper.items import NewsScraperItem

class NewsSpider(scrapy.Spider):
    name = "news"

    start_urls = ['https://zeenews.india.com/latest-news']
    
    def start_requests(self):
        urls = ['https://zeenews.india.com/latest-news']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):


        item = NewsScraperItem()
        
        data = response.css('div.sec-con-box')

        item['headlines'] = data.css('h3::text').extract_first()

        item['content'] = data.css('p::text').extract_first()

        yield item

