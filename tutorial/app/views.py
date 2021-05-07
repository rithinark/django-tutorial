from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import Register
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.POST:
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
    else:
        form = Register()
        print([type(fo) for fo in form])
    return render(request,'app\\index.html',{'forms':form})