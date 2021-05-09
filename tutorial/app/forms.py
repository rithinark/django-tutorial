from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User._meta.get_field('email')._unique = True
class Register(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            'id': 'InputUname',
            'placeholder': 'User Name'}),
        max_length = 32, 
        label="User Name",
        label_suffix="")

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            'id': 'InputFname',
            'placeholder': 'FIrst Name'}),
        max_length = 32, 
        label="First Name",
        label_suffix="")

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            'id': 'InputLname',
            'placeholder': 'Last Name'}), 
        max_length = 32, 
        label="Last Name",
        label_suffix="")

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
            'id': 'InputEmail',
            'placeholder': 'Email Address'}), 
        max_length=254, 
        label="Email Address",
        label_suffix="")

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
            'id': 'InputPassword',
            'placeholder': 'Password'}), 
        label="Password",
        label_suffix="")

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
        'id': 'InputPassword',
        'placeholder': 'Confirm Password'}), 
        label="Confirm Password",
        label_suffix="")
        
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class Login(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 
            'id': 'InputEmail',
            'placeholder':'Email Address'}), 
        max_length=254, 
        label="Email Address",
        label_suffix="")

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 
            'id': 'InputPassword',
            'placeholder':'Password'}), 
        label="Password",
        label_suffix="")
    
