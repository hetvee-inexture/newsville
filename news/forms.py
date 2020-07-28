from django import forms

NEWS_CHOICES = [
    ('NDTV','NDTV'),
    ('ZEE','ZEE'),
    ('SCROLL','SCROLL')
]
TYPE_CHOICE = [
    ('latest_news','Lates News'),
    ('world_news','World News'),
    ('cricket_news','Cricket News'),
    ('city_news','State/City News'),
    ('ent_news','Enatertainment News'),
    ('country_news','India News')
]

class Choices(forms.Form):
    NEWS_CHOICES = forms.CharField(widget=forms.RadioSelect(choices=NEWS_CHOICES))
    TYPE_CHOICE = forms.CharField(widget=forms.RadioSelect(choices=TYPE_CHOICE))