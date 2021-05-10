from django.urls import path ,re_path
from django.contrib.auth import views as auth_views
from .forms import auth_forms
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from . import views

urlpatterns = [
    path('', views.Regist_page),
    re_path('signup',views.Regist_page),
    path('login',views.Login_page, name="loginPage"),
    re_path(r'logout/$', views.Logout_page,name='logout'),
    re_path(r'^home/$', views.home, name="home")  
]

urlpatterns+= [
    path('reset-password', auth_forms.MyPasswordResetView.as_view(
        template_name="app/auth_templates/password_reset.html"), name="password_reset"
    ),

    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='app/auth_templates/password_reset_done.html'),
        name='password_reset_done'
    ),

    path('password-reset-confirm/<uidb64>/<token>/', auth_forms.MyPasswordResetConfirmView.as_view(
        template_name="app/auth_templates/password_reset_confirm.html"),
        name="password_reset_confirm"
    ),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/auth_templates/password_reset_complete.html'),
        name='password_reset_complete'
    ),

]