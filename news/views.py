from django.shortcuts import render,redirect
from news.models import LatestNews

def headlines(request):

    context = {
        'latest_news': LatestNews.objects.all()
    }

    print(context['latest_news'][0].latest_content)
 
    return render(request, 'news/headlines.html',context)

def state_news(request):


    return render(request, 'news/state_news.html')

def country_news(request):


    return render(request, 'news/country_news.html')

def sports_news(request):

    return render(request, 'news/sports_news.html')

def political_news(request):
     
     return render(request, 'news/political_news.html')


