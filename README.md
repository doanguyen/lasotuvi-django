Mã nguồn mở chương trình an sao Tử vi lasotuvi
===========================================

This is a wrapper of lasotuvi into django application.


1. Create virtual environment and activate it

* `pip install virtualenv`

* `virtualenv .env`

* If you are *nix users

`source .env/bin/activate`

* if you are Window users, just type

`.env/Scripts/activate.bat` and make sure you are working on command prompt (cmd.exe) not PowerShell


2. Now you are working on the virtual environment

* If you do not have Django project, go and install django and lasotuvi applications

`pip install django lasotuvi-django`

* If you have django project already, just install the lasotuvi-django application

`pip install lasotuvi-django`

3. Add the `lasotuvi-django` application to your INSTALLED_APPS
by adding 

```
# settings.py
INSTALLED_APPS = [
    # Your others applications 
    'lasotuvi_django',
]
```

4. Add router to the `urls.py`

```
# urls.py
from django.urls import path, include

urlpatterns = [
    # ....
    path('lasotuvi/', include('lasotuvi_django.urls'))
]

```


Here is a tutorial to show you how to add lasotuvi app into a django project.

[![Tutorial](http://i.vimeocdn.com/video/717548888_640.jpg)](https://vimeo.com/283303258 "Tutorial")

Hope this help!
