from django.core import validators
from django import forms
from .models import User

class Include(forms.ModelForm):
    class Meta:
        model=User
        fields=['celebrity', 'movie', 'imdb']
        widgets={
            'celebrity':forms.TextInput(attrs={'class':'form-control'}),
            'movie':forms.TextInput(attrs={'class':'form-control'}),
            'imdb':forms.TextInput(attrs={'class':'form-control'}),
        }