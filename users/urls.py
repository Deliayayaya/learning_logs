from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    # path('/login', LoginView, {'template_name': 'users/login.html'}, name='login')
    path('login/', LoginView.as_view(template_name= 'users/login.html'),name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/',views.register, name='register')
]