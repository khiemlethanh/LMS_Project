from django.shortcuts import render,redirect
from .models import Author,Book,Issue,Fine
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def Mylibrary(request):
    return render(request, 'Students/Mylibrary.html')

def Dashboard(request):
    return render(request,'Students/DashBoard.html')

def Returnbook(request):
    return render(request, 'Students/Returnbook.html')

def Setting(request):
    return render(request, 'Students/Setting.html')