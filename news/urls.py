from django.urls import path, include
from .views import (home, add_tag, 
ndtv_news, zee_news, 
scroll_news, add_headline)

#news url patterns

urlpatterns = [
    path('', home,name='home'),
    path('add-tag/', add_tag, name='add-tag'),
    path('add-headline/', add_headline, name='add-headline'),
    path('ndtv-news/', ndtv_news, name='ndtv-news'),
    path('zee-news/', zee_news, name='zee-news'),
    path('scroll-news/', scroll_news, name='scroll-news'),
]