from django.db import models
import json
from django.utils import timezone

# news models
class NdtvNews(models.Model):
    ndtv_headlines = models.TextField()
    ndtv_content = models.TextField()
    ndtv_img_url = models.TextField()

class NdtvLatestNews(models.Model):
    news_id = models.ForeignKey(NdtvNews, on_delete=models.CASCADE)

class NdtvWorldNews(models.Model):
    news_id = models.ForeignKey(NdtvNews, on_delete=models.CASCADE)

class NdtvCricketNews(models.Model):
    news_id = models.ForeignKey(NdtvNews, on_delete=models.CASCADE)

class NdtvCityNews(models.Model):
    news_id = models.ForeignKey(NdtvNews, on_delete=models.CASCADE)

class NdtvEntNews(models.Model):
    news_id = models.ForeignKey(NdtvNews, on_delete=models.CASCADE)

class NdtvCountryNews(models.Model):
    news_id = models.ForeignKey(NdtvNews, on_delete=models.CASCADE)

class ScrollNews(models.Model):
    scroll_headlines = models.TextField()
    scroll_content = models.TextField()
    scroll_img_url = models.TextField()

class ScrollLatestNews(models.Model):
    news_id = models.ForeignKey(ScrollNews, on_delete=models.CASCADE)

class ScrollWorldNews(models.Model):
    news_id = models.ForeignKey(ScrollNews, on_delete=models.CASCADE)

class ScrollCountryNews(models.Model):
    news_id = models.ForeignKey(ScrollNews, on_delete=models.CASCADE)

class ScrollEntNews(models.Model):
    news_id = models.ForeignKey(ScrollNews, on_delete=models.CASCADE)

class ScrollCricketNews(models.Model):
    news_id = models.ForeignKey(ScrollNews, on_delete=models.CASCADE)

class ScrollCityNews(models.Model):
    news_id = models.ForeignKey(ScrollNews, on_delete=models.CASCADE)

class ZeeNews(models.Model):
    zee_headlines = models.TextField()
    zee_content = models.TextField()
    zee_img_url = models.TextField()

class ZeeCountryNews(models.Model):
    news_id = models.ForeignKey(ZeeNews, on_delete=models.CASCADE)

class ZeeCricketNews(models.Model):
    news_id = models.ForeignKey(ZeeNews, on_delete=models.CASCADE)

class ZeeLatestNews(models.Model):
    news_id = models.ForeignKey(ZeeNews, on_delete=models.CASCADE)

class ZeeWorldNews(models.Model):
    news_id = models.ForeignKey(ZeeNews, on_delete=models.CASCADE)

#Tags models and relations
class Tags(models.Model):
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.tags

class NewsTag(models.Model):
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)
    news_id = models.IntegerField()

class Headlines(models.Model):
    headlines = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg',upload_to='headline_image')
    description = models.TextField()

    def  __str__(self):
        return self.headlines
    

class NewsHeadlines(models.Model):
    headlines_id = models.ForeignKey(Headlines, on_delete=models.CASCADE)
    news_id = models.IntegerField()

