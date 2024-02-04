from django import forms
from django.forms import ModelForm 
from .models import *




class BootstrapImageWidget(forms.ClearableFileInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control shadow rouded-0'} 
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs) 

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article 
        fields=('category','title','content','image')

        widget={
            'category':forms.TextInput(attrs={'class': 'form-control shadow rounded-0','placeholder': 'Select a Category'}),
            'title': forms.TextInput(attrs={'class':'form-control shadow rounded-0'}),
            'content': forms.Textarea(attrs={'rows':'8', 'cols':'10','class':'form-control shadow rouded-0'}), 
        }