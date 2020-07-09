from django.shortcuts import render,redirect
from news.models import (LatestNews,CountryNews,
                        CricketNews, WorldNews, 
                        StateNews, StateOneliners,
                        EntNews,EntOneliners)

def headlines(request):

    context = {
        'latest_news': LatestNews.objects.all()
    }
    return render(request, 'news/headlines.html',context)

def state_news(request):


    return render(request, 'news/state_news.html')

def country_news(request):

    context = {
        'country_news': CountryNews.objects.all()
    }

    return render(request, 'news/country_news.html',context)

def cricket_news(request):

    context = {
        'cricket_news': CricketNews.objects.all()
    }

    return render(request, 'news/sports_news.html',context)

def world_news(request):

    context = {
        'world_news': WorldNews.objects.all()
    }
     
    return render(request, 'news/world_news.html',context)

def state_news(request):

    context = {
        'state_news': StateNews.objects.all(),
        'state_oneliners': StateOneliners.objects.all()
    }
     
    return render(request, 'news/state_news.html',context)

def ent_news(request):

    context = {
        'ent_news': EntNews.objects.all(),
        'ent_oneliners': EntOneliners.objects.all()
    } 

    return render(request, 'news/ent_news.html',context)


