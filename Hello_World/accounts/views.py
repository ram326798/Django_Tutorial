import re
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # print("Username already taken")
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # print("Email already taken")
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                # print("User created")
                # messages.info(request, 'User Registered Successfully')
                return redirect('login')
        else:
            # print("password is not matching ...")
            messages.info(request, 'Password is not Matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if(user is not None):
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(reqest):
    auth.logout(reqest)
    return redirect('/')
