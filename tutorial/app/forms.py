from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User._meta.get_field('email')._unique = True
class Register(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'InputUname'}), max_length = 32, label="User Name")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'InputFname'}), max_length = 32, label="First Name")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'InputLname'}), max_length = 32, label="Last Name")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'InputEmail'}), max_length=254, label="Email Address")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'InputPassword'}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'InputPassword'}), label="Confirm Password")
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class Login(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'InputEmail'}), max_length=254, label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'InputPassword'}), label="Password")
    
