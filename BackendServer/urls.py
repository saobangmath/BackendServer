"""BackendServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    url('index/', views.home, name='home'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),
    url('register/', views.register, name='register'),
    url('checkprogress/', views.checkprogress, name='checkprogress'),
    url(r'^admin/', admin.site.urls),
    path('questions/', include('questions.urls'), name='questions'),
    path('levels/', include('levels.urls'), name='levels'),
    path('attempts/', include('attempts.urls'), name='attempts'),
    path('worlds/', include('worlds.urls'), name='worlds'),
    path('users/', include('users.urls'), name='users'),
]

# path('', include('home.urls')),