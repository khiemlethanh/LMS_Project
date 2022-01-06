from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard',views.Dashboard,name='Dashboard'),
    path('Mylibrary',views.Mylibrary,name='Mylibrary'),
    path('Returnbook',views.Returnbook,name='Returnbook'),
    path('Setting',views.Setting,name='Setting')
]