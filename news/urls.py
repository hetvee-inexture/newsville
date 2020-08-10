from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('add-tag/', add_tag, name='add-tag'),
    path('ndtv-news/', ndtv_news, name='ndtv-news'),
    path('zee-news/', zee_news, name='zee-news'),
    path('scroll-news/', scroll_news, name='scroll-news'),
]