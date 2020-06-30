from django.db import models
import json
from django.utils import timezone

class LatestNews(models.Model):
    unique_id = models.CharField(max_length=100)
    headlines = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.unique_id
