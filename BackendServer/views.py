from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


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
                request.PATH_INFO = ''
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                print('user created ', username)
                return redirect('/')
        else:
            # throw error
            print('password not matching')
            request.PATH_INFO = ''
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')


def login(request):
    request.PATH_INFO = '/login/'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


    else:

        return render(request, 'login.html')

def home(request):
    # return HttpResponse("Hello World")
    # print('home',request)
    return render(request, 'index.html')

def about(request):
    request.PATH_INFO='/about/'
    return render(request, 'about.html')

def services(request):
    request.PATH_INFO = '/services/'
    return render(request, 'services.html')

def portfolio(request):
    request.PATH_INFO = '/portfolio/'
    return render(request, 'portfolio.html')

def price(request):
    request.PATH_INFO = '/price/'
    return render(request, 'price.html')