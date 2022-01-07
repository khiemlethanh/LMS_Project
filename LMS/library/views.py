from django.shortcuts import render,redirect
from .models import Book,Author,Issue,Fine
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.utils import timezone
import datetime
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth
from core import settings

def Mylibrary(request):
    book = Book.objects.all()   
    return render(request, 'Students/Mylibrary.html', 
    {'book': book})

# def sort(request):
#     selectField=request.GET.get('selectField')
#     # sort_by=request.GET.get('sort')
#     # requestedbooks,issuedbooks=getmybooks(request.user)
#     if 'Name' in selectField:
#         book_results=Book.objects.all().order_by('name')
#         return render(request,'Students/Mylibrary.html',{'author_results':book_results,'selected':'name'})
#     if 'Author' in selectField:
#         Author_results=Book.objects.all().order_by('Author')
#         return render(request,'Students/Mylibrary.html',{'books_results': Author_results,'selected':'Author'})
#     if 'Type' in selectField:
#         Tbook_results=Book.objects.all().order_by('Type')
#         return render(request,'Students/Mylibrary.html',{'author_results':Tbook_results,'selected':'type'})



def Dashboard(request):
    book = Book.objects.all()[:8]
    return render(request,'Students/DashBoard.html',
    {'book': book})

def Returnbook(request):
    student = Student.objects.get(student_id = request.user)
    issue = Issue.objects.filter(student_id = student).select_related('book')

    return render(request, 'Students/Returnbook.html',
    {'issue': issue})

def Setting(request):
    student=Student.objects.get(student_id=request.user)
    name = student.last_name + " " + student.first_name

    return render(request, 'Students/Setting.html',
    {'cur_user': student, 'name': name})
    
