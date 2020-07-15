from django.test import TestCase, Client
from django.urls import reverse
from news.models import (CountryNews,CricketNews, 
LatestNews,WorldNews, 
EntNews,EntOneliners,
StateNews,StateOneliners)
import json

class TestViews(TestCase):

    def test_country_view_GET(self):
        client = Client()
        response = client.get(reverse('country-news'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'news/country_news.html')
