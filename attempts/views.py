from django.shortcuts import render
from django import http
# Create your views here.
def index(request):
    return render(request, 'attempts/index.html')