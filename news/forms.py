from django import forms
from news.models import Tags, NewsTag, Headlines, NewsHeadlines

#Form for adding new tags and selcting existing ones
class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tags']

class NewsTagForm(forms.ModelForm):
    class Meta:
        model = NewsTag
        fields = ['tag_id']

class HeadlinesForm(forms.ModelForm):
    class Meta:
        model = Headlines
        fields = ['headlines', 'image', 'description']

class NewsHeadlinesForm(forms.ModelForm):
    class Meta:
        model = NewsHeadlines
        fields = ['headlines_id']

    