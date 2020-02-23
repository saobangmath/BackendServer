from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    request.PATH_INFO = '/register/'
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username taken', username)
                messages.info(request, 'username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                print('user created ', username)
                return redirect('login')
                # create new page for successful registration
        else:
            # throw error
            print('password not matching')
            messages.info(request, 'password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    request.PATH_INFO = '/login/'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        # not none if authenticated

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    # return HttpResponse("Hello World")
    # print('home',request)
    return render(request, 'index.html')

# put @login_required before every page that needs login to be accessed
@login_required
def checkprogress(request):
    return render(request, 'checkprogress.html')


