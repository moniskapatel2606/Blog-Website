from django import forms
from django.forms import ModelForm 
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article 
        fields='__all__'

        widget={
            'category':forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'rows':'8','cols':'10','class':'form-control'}),
        }