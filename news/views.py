from django.shortcuts import render,redirect
from news.models import (LatestNews,CountryNews,
                        CricketNews, WorldNews, 
                        StateNews, StateOneliners,
                        EntNews,EntOneliners, NdtvlatestNews,
                        NdtvCountryNews,NdtvWorldNews,
                        NdtvCricketNews,NdtvEntNews,
                        ScrollLatestNews,ScrollCityNews,
                        ScrollCountryNews,ScrollCricketNews,
                        ScrollEntNews,ScrollWorldNews)
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def headlines(request):


    context = {
        'latest_news': ScrollLatestNews.objects.all()
    }
    return render(request, 'news/headlines.html',context)

@login_required
def content(request):
    context = {
        'latest_news': ScrollLatestNews.objects.all()
    }

    return render(request, 'news/home.html',context)

    
@login_required
def country_news(request):

    context = {
        'country_news': ScrollCountryNews.objects.all()
    }

    return render(request, 'news/country_news.html',context)

@login_required
def cricket_news(request):

    context = {
        'cricket_news': ScrollCricketNews.objects.all()
    }

    return render(request, 'news/sports_news.html',context)

@login_required
def world_news(request):

    context = {
        'world_news': ScrollWorldNews.objects.all()
    }
     
    return render(request, 'news/world_news.html',context)

@login_required
def state_news(request):

    context = {
        'state_news': StateNews.objects.all(),
        'state_oneliners': StateOneliners.objects.all()
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
    