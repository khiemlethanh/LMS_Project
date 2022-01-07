from django.shortcuts import render,redirect
from .models import Student,Department 
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request,
                                 username=request.POST['username'], 
                                 password=request.POST['password'])
        print(user)                        
        if user is None:
            messages.error(request,'Login fail try agian!')
            return redirect('Login')
        else:
            auth.login(request, user)
            # messages.success(request,'Login successful')
            # if 'next' in request.POST:
            #     return redirect(request.POST['next'])
            return redirect('Dashboard') 
    else:
        return render(request, 'Login.html')
