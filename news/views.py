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
from news.forms import Choices
global TYPE

def home(request):

    return render(request, 'news/home.html')

def headlines(request):
    global TYPE

    if request.GET.get('ndtv'):

        context = {
            'latest_news': NdtvlatestNews.objects.all()
        }
        TYPE = 'NDTV'
        return render(request, 'news/headlines.html',context)
    
    if request.GET.get('zee'):
        context = {
            'latest_news': LatestNews.objects.all()
        }
        TYPE = 'ZEE'
        return render(request, 'news/headlines.html',context)

    if request.GET.get('scroll'):
        context = {
            'latest_news': ScrollLatestNews.objects.all()
        }
        TYPE = 'SCROLL'
        return render(request, 'news/headlines.html',context)


    
@login_required
def country_news(request):
    global TYPE

    if TYPE == 'NDTV':

        context = {
            'country_news': NdtvCountryNews.objects.all()
        }

        return render(request, 'news/country_news.html',context)

    if TYPE == 'ZEE':
        
        context = {
            'country_news': CountryNews.objects.all()
        }

        return render(request, 'news/country_news.html',context)
    else:
        print(TYPE)
        context = {
            'country_news': ScrollCountryNews.objects.all()
        }

        return render(request, 'news/country_news.html',context)

@login_required
def cricket_news(request):
    global TYPE
    if TYPE == 'NDTV':    
        context = {
            'cricket_news': NdtvCricketNews.objects.all()
        }

        return render(request, 'news/sports_news.html',context)
    elif TYPE =='ZEE':
        context = {
            'cricket_news': CricketNews.objects.all()
        }

        return render(request, 'news/sports_news.html',context)
    else:
        context = {
            'cricket_news': ScrollCricketNews.objects.all()
        }

        return render(request, 'news/sports_news.html',context)

@login_required
def world_news(request):
    global TYPE
    if TYPE == 'NDTV':
        print(TYPE)
        context = {
            'world_news': NdtvWorldNews.objects.all()
        }
        
        return render(request, 'news/world_news.html',context)

@login_required
def state_news(request):

    if TYPE == 'ZEE':

        context = {
            'state_news': StateNews.objects.all(),
            'state_oneliners': StateOneliners.objects.all()
        }

    elif TYPE == 'NDTV':
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

    # context = {
    #     'ent_news': EntNews.objects.all(),
    #     'ent_oneliners': EntOneliners.objects.all()
    # } 
    context = {
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


    print(context)
    return render(request, 'news/search.html',context)
    