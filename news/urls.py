from django.urls import path, include
from .views import (headlines, state_news, country_news, political_news, sports_news)

urlpatterns = [
    path('', headlines,name='headlines'),
    path('state-news/',state_news,name='state-news'),
    path('country-news/', country_news, name='country-news'),
    path('political-news/', political_news, name='political-news'),
    path('sports-news/', sports_news, name='sports-news')
]