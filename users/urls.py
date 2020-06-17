from django.urls import path, include
from .views import register, hello
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('', hello, name='hello'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]