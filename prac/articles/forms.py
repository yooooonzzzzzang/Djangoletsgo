# ----------------그냥 평범 폼------------
# from django import forms

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)

from django import forms
from .models import article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = article
        fields = '__all__'