from django.shortcuts import render,redirect


def headlines(request):

    return render(request, 'news/headlines.html')

def state_news(request):


    return render(request, 'news/state_news.html')

def country_news(request):


    return render(request, 'news/country_news.html')

def sports_news(request):

    return render(request, 'news/sports_news.html')

def political_news(request):
     
     return render(request, 'news/political_news.html')


