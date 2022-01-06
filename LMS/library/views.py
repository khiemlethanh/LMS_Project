from django.shortcuts import render
import calendar
from datetime import datetime
from .models import Book

def Mylibrary(request):
    book = Book.objects.all()
    return render(request, 'Students/Mylibrary.html', 
    {'book': book})

def Dashboard(request):
    book = Book.objects.all()
    return render(request,'Students/DashBoard.html',
    {'book': book})

def Returnbook(request):
    return render(request, 'Students/Returnbook.html')

def Setting(request):
    return render(request, 'Students/Setting.html')
    
