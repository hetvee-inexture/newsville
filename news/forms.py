from django import forms
from news.models import Tags


class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tags']