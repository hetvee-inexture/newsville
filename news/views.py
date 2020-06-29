from django.shortcuts import render,redirect
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import os

def headlines(request):
    os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "home/hetvee/Desktop/Hetvee/newsville/news_scraper/news_scraper/settings.py")
    crawler_settings = get_project_settings()
    crawler = CrawlerRunner(crawler_settings)
    crawler.crawl(NewsSpider)
    return render(request, 'news/headlines.html')

def state_news(request):


    return render(request, 'news/state_news.html')

def country_news(request):


    return render(request, 'news/country_news.html')

def sports_news(request):

    return render(request, 'news/sports_news.html')

def political_news(request):
     
     return render(request, 'news/political_news.html')


