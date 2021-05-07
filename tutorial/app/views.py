from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Register,Login
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    if request.POST:
        form = Register(request.POST)
        if form.is_valid():
            form.save()
                return HttpResponse("""welcome to the website
                <a href='logout'>Logout</a>""")
    else:
        form = Register()
    return render(request,'app\\index.html',{'forms':form})

def Login_page(request):
    if request.POST:
        form = Login(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("""welcome to the website
                <a href='logout'>Logout</a>""")
            else:
                message="invalid username or password"
        else:
            message="invalid username or password"
    else:
        form = Login()
        message=""
    return render(request, 'app/login.html', {'forms':form,'message':message})

def Logout_page(request):
    logout(request)
    return redirect('loginPage')