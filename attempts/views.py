from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import http
# Create your views here.
@login_required
def index(request):
    return render(request, 'attempts/index.html')