from django.shortcuts import render,redirect
from news.models import LatestNews

def headlines(request):
    # news_obj = LatestNews.objects.all()
    # context = {
    #     'headlines': news_obj.headlines,
    #     'content': news_obj.content,
    #     'date': news_obj.date
    # }
    return render(request, 'news/headlines.html')

def state_news(request):


    return render(request, 'news/state_news.html')

def country_news(request):


    return render(request, 'news/country_news.html')

def sports_news(request):

    return render(request, 'news/sports_news.html')

def political_news(request):
     
     return render(request, 'news/political_news.html')


