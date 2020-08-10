from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('ent-news/', ent_news, name='ent-news'),
    # path('content/',content, name='home'),
    path('search/', headlines_search, name='search'),
    path('add-tag/', add_tag, name='add-tag'),
    path('ndtv-news/', ndtv_news, name='ndtv-news'),
    path('zee-news/', zee_news, name='zee-news'),
    path('scroll-news/', scroll_news, name='scroll-news'),
]