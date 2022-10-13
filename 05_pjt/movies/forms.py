from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
    CHOICES = (('COMEDY', 'COMEDY'),('HOROR', 'HOROR'),('ROMANCE', 'ROMANCE'),)
    
    genre = forms.CharField(max_length=30,widget=forms.widgets.Select(choices=CHOICES))

    score =forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step': 0.5,
                'min': 0,
                'max': 5,
            }
        )
    )
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

