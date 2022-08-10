from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'Password does not match!')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password  )

        if user is not None:
            auth.login(request , user)
            return redirect('/')    
        else:
            messages.info(request, 'Invalid username or password')
            return redirect("/")
    else:
        return render(request,'login.html')
    
def logout_request(request):

    logout(request)
    return redirect('news')
