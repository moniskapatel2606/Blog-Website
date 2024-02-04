from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class NewRegisterForm(UserCreationForm):

    email=forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'Enter your Email', 'class':'form-control'}))
    username=forms.CharField( max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Enter your Name', 'class':'form-control'}))
    password1=forms.CharField(label='password',required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Re-Enter password',required=True, widget=forms.PasswordInput(attrs={ 'class':'form-control'}))


    # User id already define in admin just need to impliment in meta class 
    class Meta:
        model=User

        fields=('username','email','password1','password2')
    def save(self,commit=True):
        user=super(NewRegisterForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user 

