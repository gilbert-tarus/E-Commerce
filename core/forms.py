from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput( attrs={
        'placeholder' : "Your username",
        'class': 'box-border w-full max-w-full py-4 px-6 rounded-xl'
        }))
    password = forms.CharField(widget=forms.PasswordInput( attrs={
        'placeholder' : "Enter password", 
        'class': "box-border max-w-full w-full py-4 px-6 rounded-xl"
        }))
class SigupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
    username = forms.CharField(widget=forms.TextInput( attrs={
        'placeholder' : "Your username",
        'class': 'box-border max-w-full w-full py-4 px-6 rounded-xl'
        }))
    email = forms.CharField(widget=forms.EmailInput( attrs={
        'placeholder' : "Your email",
        'class': "box-border max-w-full w-full py-4 px-6 rounded-xl"
        }))
    password1 = forms.CharField(widget=forms.PasswordInput( attrs={
        'placeholder' : "Enter password", 
        'class': "box-border max-w-full w-full py-4 px-6 rounded-xl"
        }))
    password2 = forms.CharField(widget=forms.PasswordInput( attrs={
        'placeholder' : "Repeat password",
        'class': "box-border max-w-full w-full py-4 px-6 rounded-xl"
        }))