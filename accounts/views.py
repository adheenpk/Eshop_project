from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def account(request):
    return render(request,'account.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('account')  # Redirect to the homepage after login
        else:
            messages.error(request, 'Invalid username or password')  # Error message
            return redirect('login')  # Redirect back to the login page

    return render(request, 'account.html')  # Render the login form


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Password do not match.')
            return redirect('register')

        if User.objects.filter(username = username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')
        if User.objects.filter(email = email).exists():
            messages.error(request, 'Email alreay taken.')
            return redirect('register')

        user=User.objects.create_user(username=username,email=email,password=password,password1=confirm_password)
        user.save();
        messages.success(request,' User created successfully! ')
        return redirect('/')
    else:
        return render(request,'account.html')
