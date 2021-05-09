from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Register,Login
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def Regist_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.POST:
            form = Register(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = Register()
        return render(request,'app\\index.html',{'form_type':'regist','forms':form})

def Login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.POST:
            form = Login(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    message="invalid username or password"
            else:
                message="invalid username or password"
        else:
            form = Login()
            message=""
        return render(request, 'app/index.html', {'form_type':'login','forms':form,'message':message})

def Logout_page(request):
    logout(request)
    return redirect('loginPage')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'app/home.html')
    else:
        return redirect('loginPage')