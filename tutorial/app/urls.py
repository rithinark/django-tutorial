from django.urls import path
from . import views

urlpatterns = [
    path('', views.Regist_page),
    path('signup',views.Regist_page),
    path('login',views.Login_page, name="loginPage"),
    path('logout', views.Logout_page),
    path('home', views.home, name="home")
    
]