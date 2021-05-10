from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import password_validation

class Register(UserCreationForm):
    """
    Display the registration form based on given fields
    """
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
    """
    Display the login form based on the given fields
    """
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


    
class MypasswordChangeForm(PasswordChangeForm):
    """
    Display the password reset form based on given fields
    """
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
        'id': 'InputPassword',
        'placeholder': 'Old Password'}), 
        label="Old Password",
        label_suffix="")

    new_password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
        'id': 'InputPassword',
        'placeholder': 'New Password'}), 
        label="New Password",
        label_suffix="")

    new_password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
        'id': 'InputPassword',
        'placeholder': 'Confirm Password'}), 
        label="Confirm Password",
        label_suffix="")
    
class PasswordChange(PasswordChangeView):
    form_class = MypasswordChangeForm




class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email Adress",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'form-control',
        })
    )

class MyPasswordResetView(PasswordResetView):
    form_class = MyPasswordResetForm



class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label= "New password",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label= "New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
        }),
    )

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = MySetPasswordForm

