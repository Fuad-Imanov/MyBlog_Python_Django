from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150,widget= forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password1','password2']
        # widgets = {
        #     'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password2'}),
        # }

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150,widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class':'form-control'}))