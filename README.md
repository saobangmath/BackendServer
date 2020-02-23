# BackendServer


(Ivan 23 feb)
Currently using html template from web. Template stored in folder 'pages'. To use, add 'pages' to STATICFILES_DIRS in settings.py
At start of EVERY html file, write
```{% load static %}```
and everytime a file is mentioned e.g.
```
<link rel="stylesheet" href="css/linearicons.css">
<img src="img/MK.png">
```
add {% static '<stuff here>' %} like
```
<link rel="stylesheet" href="{% static 'css/linearicons.css' %}">
<img src="{% static 'img/MK.png' %}">
```
using single quotes to avoid escaping. (Yes I know this is a massive burden but I dont know how to work around this)
