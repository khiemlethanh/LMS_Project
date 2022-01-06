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
<<<<<<< Updated upstream
=======

def search(request):
    search_query=request.GET.get('search-query')
    search_by_author=request.GET.get('author')
    requestedbooks,issuedbooks=getmybooks(request.user)

    if search_by_author is not None:
        author_results=Author.objects.filter(name__icontains=search_query)
        return render(request,'library/home.html',{'author_results':author_results,'issuedbooks':issuedbooks,'requestedbooks':requestedbooks})
    else:
        books_results=Book.objects.filter(Q(name__icontains=search_query) | Q(category__icontains=search_query))
        return render(request,'library/home.html',{'books_results':books_results,'issuedbooks':issuedbooks,'requestedbooks':requestedbooks})
>>>>>>> Stashed changes
