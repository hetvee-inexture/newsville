from django.urls import path, include
from .views import (headlines, state_news, 
                    country_news, world_news, 
                    cricket_news,ent_news)

urlpatterns = [
    path('', headlines,name='headlines'),
    path('state-news/',state_news,name='state-news'),
    path('country-news/', country_news, name='country-news'),
    path('world-news/', world_news, name='world-news'),
    path('sports-news/', cricket_news, name='sports-news'),
    path('ent-news/', ent_news, name='ent-news'),
]