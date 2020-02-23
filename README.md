# BackendServer


(Ivan 23 feb)
Currently using html template from web. Template stored in folder 'pages'. To use, add 'pages' to STATICFILES_DIRS in settings.py
At start of EVERY html file, write
```{% load static %}```
and everytime a file is mentioned e.g.
```
<img src="img/MK.png">
```
add {% static '<stuff here>' %} like
```

<img src="{% static 'img/MK.png' %}">
```
using single quotes to avoid escaping. (Yes I know this is a massive burden but I dont know how to work around this)




For every page added, add to urls.py, and create function in views.py. Add ```@login_required```  before function in views.py for pages that require login (probably all from here on)
For each page that is not index (home), make sure all links start with ```../``` and home is referenced as <empty string> instead of ```index```.
