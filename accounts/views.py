from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def sign_up(request):
    if request.method == 'POST':
        # The user has info and wants to create an account
        if request.POST['password'] == request.POST['confirmpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/sign_up.html', {'error': 'Username already taken, Try another!'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            # wrong password in confirm password
            return render(request, 'accounts/sign_up.html', {'error': 'Password must match!'})

    else:
        # User just came for signup!
        return render(request, 'accounts/sign_up.html')


def login(request):
    if request.method == 'POST':
        # user has filled the infos
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password! Please try again!'})
    else:
        # User wants to login
        return render(request, 'accounts/login.html')


def logout(request):
    # TODO need to rerout to home page and to Logout
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
