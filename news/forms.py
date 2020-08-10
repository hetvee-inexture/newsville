from django import forms
from news.models import Tags, NewsTag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tags']

class NewsTagForm(forms.ModelForm):
    class Meta:
        model = NewsTag
        fields = ['tag_id']