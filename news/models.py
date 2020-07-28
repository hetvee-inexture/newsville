from django.db import models
import json
from django.utils import timezone

class CountryNews(models.Model):

    country_headlines = models.TextField()
    country_content = models.TextField()
    country_image_url = models.TextField()
    date = models.DateTimeField(default=timezone.now, null=True)


    def __str__(self):
        return self.country_headlines

class CricketNews(models.Model):

    cricket_headlines = models.TextField()
    cricket_content = models.TextField()
    cricket_image_url = models.TextField()
    date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.cricket_headlines

class LatestNews(models.Model):

    latest_headlines = models.TextField()
    latest_content = models.TextField()
    latest_image_url = models.TextField()
    date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.latest_headlines

class WorldNews(models.Model):

    world_headlines = models.TextField()
    world_content = models.TextField()
    world_image_url = models.TextField()
    date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.world_headlines


class StateNews(models.Model):

    state_lead_text = models.TextField()
    state_image_url = models.TextField()
    state_name = models.TextField()

    def __str__(self):
        return self.state_lead_text

class StateOneliners(models.Model):

    one_liners = models.TextField()
    state_id = models.ForeignKey(StateNews,on_delete=models.CASCADE)

    def __str__(self):
        return self.one_liners

class EntNews(models.Model):
    ent_lead_text = models.TextField()
    ent_image_url = models.TextField()
    ent_name = models.TextField()

    def __str__(self):
        return self.ent_lead_text

class EntOneliners(models.Model):

    one_liners = models.TextField()
    ent_id = models.ForeignKey(EntNews,on_delete=models.CASCADE)

    def __str__(self):
        return self.one_liners

class NdtvlatestNews(models.Model):

    latest_headlines = models.TextField()
    latest_content = models.TextField()
    latest_image_url = models.TextField()

    def __str__(self):
        return self.latest_headlines

class NdtvCityNews(models.Model):

    city_headlines = models.TextField()
    city_content = models.TextField()
    city_image_url = models.TextField()

    def __str__(self):
        return self.city_headlines

class NdtvCountryNews(models.Model):

    country_headlines = models.TextField()
    country_content = models.TextField()
    country_image_url = models.TextField()

    def __str__(self):
        return self.country_headlines

class NdtvWorldNews(models.Model):

    world_headlines = models.TextField()
    world_content = models.TextField()
    world_image_url = models.TextField()

    def __str__(self):
        return self.world_headlines

class NdtvCricketNews(models.Model):

    cricket_headlines = models.TextField()
    cricket_content = models.TextField()
    cricket_image_url = models.TextField()

    def __str__(self):
        return self.cricket_headlines

class NdtvEntNews(models.Model):

    ent_headlines = models.TextField()
    ent_content = models.TextField()
    ent_image_url = models.TextField()

    def __str__(self):
        return self.ent_headlines

class ScrollLatestNews(models.Model):

    latest_headlines = models.TextField()
    latest_content = models.TextField()
    latest_image_url = models.TextField()

class ScrollWorldNews(models.Model):

    world_headlines = models.TextField()
    world_content = models.TextField()
    world_image_url = models.TextField()

    def __str__(self):
        return self.world_headlines

class ScrollCountryNews(models.Model):

    country_headlines = models.TextField()
    country_content = models.TextField()
    country_image_url = models.TextField()

    def __str__(self):
        return self.country_headlines

class ScrollEntNews(models.Model):

    ent_headlines = models.TextField()
    ent_content = models.TextField()
    ent_image_url = models.TextField()

    def __str__(self):
        return self.ent_headlines

class ScrollCricketNews(models.Model):

    cricket_headlines = models.TextField()
    cricket_image_url = models.TextField()

    def __str__(self):
        return self.cricket_headlines

class ScrollCityNews(models.Model):

    city_headlines = models.TextField()
    city_image_url = models.TextField()
    def __str__(self):
        return self.city_headlines

# class Tags(models.Model):

#     tags = [
#         ('trending','Trending'),
#         ('latest', 'Latest'),
#         ('cricket', 'Cricket'),
#         ('entertaining', 'Entertaining'),
#         ('rip', 'RIP'),
#         ('india', 'India')
#     ]

#     tag_name = models.CharField(max_length=100,choices=tags)
