from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.login,name='Login'),
    path('Mylibrary',views.Mylibrary,name='Mylibrary')
]