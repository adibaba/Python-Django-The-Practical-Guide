# Section 3: URLs & Views

## Lectures

### 18. Module Introduction

- URLs = Routes

### 19. Creating a New Project

- `python -m django startproject monthly_challenges`
- `python manage.py startapp challenges`
- Command Palette (Ctrl+Shift+P) 'Python: Select Interpreter'
- Command Palette (Ctrl+Shift+P) 'Preferences: Open Workspace Settings (JSON)'  
  (Creates settings.json file)
	-  Probably optional:`{ "python.languageServer": "Pylance" }`

### 20. What are URLs & Views?

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/urls-views-zz-extra-files/slides/slides.pdf)

### 21. Creating a First View & URL

Start server: `python manage.py runserver`
- [http://localhost:8000/challenges/january](http://localhost:8000/challenges/january)
- [Docs: Intro ➝ tutorial01 ➝  creating the polls app](https://docs.djangoproject.com/en/4.2/intro/tutorial01/#creating-the-polls-app)
- [Docs: API Reference ➝ request response ➝  httpresponse objects](https://docs.djangoproject.com/en/4.2/ref/request-response/#httpresponse-objects)

### 22. Adding More Views & URLs

### 23. Dynamic Path Segments & Captured Values

- [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/urls-views-02-dynamic-path-segments)
  for urls-views-02-dynamic-path-segments
- [Docs: API Reference ➝ request response ➝  django.http.HttpResponseNotFound](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpResponseNotFound)

### 24. Path Converters

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/bb13fa8..8a353a6) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/urls-views-03-exploring-path-converters)
  for urls-views-03-exploring-path-converters
- [Docs: Topics ➝ http ➝ urls ➝  path converters](https://docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters)

### 25. Adding More Dynamic View Logic

### 26. Redirects

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/8a353a6..eeaa22d) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/urls-views-04-redirecting)
  for urls-views-04-redirecting
- [Docs: API Reference ➝ request response ➝  django.http.HttpResponseRedirect](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpResponseRedirect)

### 27. The Reverse Function & Named URLs

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/eeaa22d..e423b06) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/urls-views-05-the-reverse-function)
  for urls-views-05-the-reverse-function
- [Docs: API Reference ➝ urlresolvers ➝  reverse](https://docs.djangoproject.com/en/4.2/ref/urlresolvers/#reverse)

### 28. Returning HTML

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/e423b06..11c7c77) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/urls-views-06-returning-html-response)
  for urls-views-06-returning-html-response
- String interpolation / formatted string literals / f-strings  
  https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings

### 29. Practicing URLs, Views & Dynamic View Logic

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/11c7c77..b3a97ef) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/urls-views-07-practicing-urls-and-views)
  for urls-views-07-practicing-urls-and-views

### 30. Summary

### 31. Useful Resources & Links

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/urls-views-zz-extra-files/slides/slides.pdf)

## Summary

- Start server: `python manage.py runserver`
  [http://localhost:8000/](http://localhost:8000/)
- [Docs: Intro ➝ tutorial01](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
- [Docs: API Reference ➝ request response](https://docs.djangoproject.com/en/4.2/ref/request-response/)
- [Docs: Topics ➝ http ➝ urls](https://docs.djangoproject.com/en/4.2/topics/http/urls/)
- [Docs: API Reference ➝ urlresolvers](https://docs.djangoproject.com/en/4.2/ref/urlresolvers/)
- https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
	
### Example code: *Hello world*

[Changes](https://github.com/adibaba/Python-Django-The-Practical-Guide/compare/00e937b..cbe01bf) and
[Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/cbe01bff248a4a9f1370b7291b26f18293cbdfe9/project)

```python
# project/project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
```

```python
# project/app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```

```python
# project/app/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')
]
```

### Example code: *Multiple paths*

[Changes](https://github.com/adibaba/Python-Django-The-Practical-Guide/compare/cbe01bf..bf347f6) and
[Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/bf347f6ce83d19a654fc2cdbeff1d569d73d8db4/project)

```python
# project/app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('echo/<str:string>', views.echo, name='echo'),
]
```

```python
# project/app/views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return HttpResponse('hello world')

def echo(request, string):
    if string == 'hello':
        return HttpResponseRedirect(reverse('echo', args=['world']))
    else:
        return HttpResponse(f'<b>{string}</b>')
```

