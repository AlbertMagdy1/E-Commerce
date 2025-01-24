from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-100'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control w-100'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-100'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-100'}))

    class Meta:
        model = User
        fields= ['username', 'email', 'password1','password2']