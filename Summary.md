# Course Summary

## Section 1: Getting Started

- [Django documentation contents](https://docs.djangoproject.com/en/4.2/contents/)
- [Getting started](https://docs.djangoproject.com/en/4.2/intro/)
- [Topics](https://docs.djangoproject.com/en/4.2/topics/)
  & [How to](https://docs.djangoproject.com/en/4.2/howto/)
- [API Reference](https://docs.djangoproject.com/en/4.2/ref/)
  & [General Index](https://docs.djangoproject.com/en/4.2/genindex/)
  & [Module Index](https://docs.djangoproject.com/en/4.2/py-modindex/)

## Section 2: Course Setup

- Create project: `python -m django startproject project`
	- Creates [files](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/ef77ebb6c74a59607012b426345381a8e51e2836)
- Create app: `python manage.py startapp app`
	- Creates [new files](https://github.com/adibaba/Python-Django-The-Practical-Guide/commit/4916ace266c6d419d675087b303e075d42d81195), resulting in [all files](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/4916ace266c6d419d675087b303e075d42d81195)
- Run server: `python manage.py runserver`
	- Starts server at [127.0.0.1:8000](http://127.0.0.1:8000/)
- IDE: [Visual Studio Code](https://code.visualstudio.com)
	- Install extensions *Python* (installs *Pylance*) and *Django*
	- Show all commands: [Ctrl] + [Shift] + [P]
		- *Preferences: Open Workspace Settings (JSON)* creates `.vscode/settings.json`
	- Format document: [Shift] + [Alt] + [F]
- Additional: Create a [.gitignore](https://github.com/adibaba/Python-Django-The-Practical-Guide/blob/section-2-code/.gitignore) file
- [Example code *new app*](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/00e937b3ecdcb3c6164176cd710f7ca0373427aa) with new project, app, gitignore and vscode settings.
- Docs:
	- [Docs: API Reference ➝ django admin](https://docs.djangoproject.com/en/4.2/ref/django-admin/)  
	  manage.py

### Visual Studio Code: `.vscode/settings.json`

```json
{
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "files.associations": {
        "**/*.html": "html",
        "**/templates/**/*.html": "django-html"
    }
}
```

## Section 3: URLs & Views

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

## Section 4: Templates & Static Files

- Example code *inheritance templates*: [Changes from *multiple paths*](https://github.com/adibaba/Python-Django-The-Practical-Guide/compare/bf347f6..bb8fb8f) and [Changes from *new app*](https://github.com/adibaba/Python-Django-The-Practical-Guide/compare/00e937b..833da1e) and
  [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/833da1e145b241f3c064a904ed6155f89fc8034a/project)
- Example code *static files*: [Changes from *inheritance templates*](https://github.com/adibaba/Python-Django-The-Practical-Guide/compare/833da1e..5b1d9bf) and [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/5b1d9bf6abed1260efeb28417ddaf145d71f7c83/project)
- Docs:
	- [Docs: Topics ➝ templates](https://docs.djangoproject.com/en/4.2/topics/templates/)
	- [Docs: API Reference ➝ templates ➝ language](https://docs.djangoproject.com/en/4.2/ref/templates/language/)
	- [Docs: API Reference ➝ templates ➝ builtins](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)
	- [Docs: Topics ➝ http ➝ shortcuts](https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/)
	- [Docs: Howto ➝ static files](https://docs.djangoproject.com/en/4.2/howto/static-files/)
	- [Docs: API Reference ➝ views ➝  the 404 page not found view](https://docs.djangoproject.com/en/4.2/ref/views/#the-404-page-not-found-view)