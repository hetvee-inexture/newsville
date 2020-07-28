from django.shortcuts import render,redirect
from news.models import (LatestNews,CountryNews,
                        CricketNews, WorldNews, 
                        StateNews, StateOneliners,
                        EntNews,EntOneliners, NdtvlatestNews,
                        NdtvCountryNews,NdtvWorldNews,
                        NdtvCricketNews,NdtvEntNews,
                        ScrollLatestNews,ScrollCityNews,
                        ScrollCountryNews,ScrollCricketNews,
                        ScrollEntNews,ScrollWorldNews,
                        NdtvCityNews)
from django.contrib.auth.decorators import login_required
from django.db.models import Q
global TYPE

def home(request):

    return render(request, 'news/home.html')

def headlines(request):

    print(url_param)

    if request.GET.get('ndtv'):

        context = {
            'latest_news': NdtvlatestNews.objects.all()
        }
    
    elif request.GET.get('zee'):
        context = {
            'latest_news': LatestNews.objects.all()
        }

    else:
        context = {
            'latest_news': ScrollLatestNews.objects.all()
        }
    
    return render(request, 'news/headlines.html',context)
     
@login_required
def country_news(request):

    if request.GET.get('ndtv'):

        context = {
            'country_news': NdtvCountryNews.objects.all()
        }

    elif request.GET.get('zee'):
        
        context = {
            'country_news': CountryNews.objects.all()
        }

    else: 
        context = {
            'country_news': ScrollCountryNews.objects.all()
        }

    return render(request, 'news/country_news.html',context)

@login_required
def cricket_news(request):

    if request.GET.get('ndtv'):    
        context = {
            'cricket_news': NdtvCricketNews.objects.all()
        }

    elif request.GET.get('zee'):
        context = {
            'cricket_news': CricketNews.objects.all()
        }

    else:
        context = {
            'cricket_news': ScrollCricketNews.objects.all()
        }

    return render(request, 'news/sports_news.html',context)

@login_required
def world_news(request):

    if request.GET.get('ndtv'):
        context = {
            'world_news': NdtvWorldNews.objects.all()
        }
        
    elif request.GET.get('zee'):
        context = {
            'world_news': WorldNews.objects.all()
        }

    else:
        context = {
            'world_news': ScrollWorldNews.objects.all()
        }

    return render(request, 'news/world_news.html',context)  

@login_required
def state_news(request):

    if request.GET.get('zee'):

        context = {
            'state_news': StateNews.objects.all(),
            'state_oneliners': StateOneliners.objects.all()
        }

    elif request.GET.get('ndtv'):
        context = {
            'city': True,
            'city_news': NdtvCityNews.objects.all()
        }
    else:
        context = {
            'city': True,
            'city_news' : ScrollCityNews.objects.all()
        }    
    return render(request, 'news/state_news.html',context)
    

@login_required
def ent_news(request):

    if request.GET.get('zee'):

        context = {
            'ent_news_one': EntNews.objects.all(),
            'ent_oneliners': EntOneliners.objects.all()
        } 
    elif request.GET.get('ndtv'):
        context = {
            'ent': 'ent',
            'ent_news': NdtvEntNews.objects.all()
        }
    else:
        context = {
            'ent' : 'ent',
            'ent_news': ScrollEntNews.objects.all()
        }

    return render(request, 'news/ent_news.html',context)

def headlines_search(request):
    headlines = LatestNews.objects.all()
    query = request.GET.get('q')
    if query:
        headlines = LatestNews.objects.filter(
            Q(latest_headlines__search=query)
        )

    context = {
        'search_filter': headlines
    }

    return render(request, 'news/search.html',context)
    