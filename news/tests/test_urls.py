from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import (headlines,content,
                        state_news,country_news,
                        world_news,cricket_news,ent_news)

class TestUrls(SimpleTestCase):

    def test_headlines_url_is_resolved(self):
        url = reverse('headlines')
        self.assertEquals(resolve(url).func, headlines)

    def test_content_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, content)

    def test_state_news_url_is_resolved(self):
        url = reverse('state-news')
        self.assertEquals(resolve(url).func, state_news)

    def test_country_news_url_is_resolved(self):
        url = reverse('country-news')
        self.assertEquals(resolve(url).func, country_news)

    def test_world_news_url_is_resolved(self):
        url = reverse('world-news')
        self.assertEquals(resolve(url).func, world_news)

    def test_cricket_news_url_is_resolved(self):
        url = reverse('sports-news')
        self.assertEquals(resolve(url).func, cricket_news)

    def test_ent_news_url_is_resolved(self):
        url = reverse('ent-news')
        self.assertEquals(resolve(url).func,ent_news)

