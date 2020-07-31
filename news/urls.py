from django.urls import path, include
from .views import (headlines, state_news, 
                    country_news, world_news, 
                    cricket_news,ent_news,headlines_search,home)

urlpatterns = [
    path('', home,name='home'),
    path('state-news/',state_news,name='state-news'),
    path('country-news/', country_news, name='country-news'),
    path('world-news/', world_news, name='world-news'),
    path('sports-news/', cricket_news, name='sports-news'),
    path('ent-news/', ent_news, name='ent-news'),
    # path('content/',content, name='home'),
    path('search/', headlines_search, name='search'),
     path('add-tag/', add_tag, name='add-tag'),
    path('ndtv-news/', ndtv_news, name='ndtv-news'),
    path('zee-news/', zee_news, name='zee-news'),
    path('scroll-news/', scroll_news, name='scroll-news'),
]