
from django.shortcuts import render,redirect
from .models import Student,Department 
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request,
                                 username=request.POST['username'], 
                                 password=request.POST['password'])
        print(user)                        
        if user is None:
            messages.error(request,'Invalid CREDENTIALS')
            return redirect('Login/')
        else:
            auth.login(request, user)
            messages.success(request,'Login successful')
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('#dashboard')
    else:
        return render(request, 'Login.html')

def Mylibrary(request):
    return render(request, 'Students/Mylibrary.html')