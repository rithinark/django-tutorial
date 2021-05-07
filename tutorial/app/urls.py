from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('login',views.Login_page, name="loginPage"),
    path('logout', views.Logout_page)
    
]