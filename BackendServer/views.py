from django.shortcuts import render
from django.http import HttpResponse

BASE_DIR = 'https://127.0.0.1:8000/'

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