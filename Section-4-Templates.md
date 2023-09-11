# Section 4: Templates

- [code](00400_templates)
- [code official](https://github.com/academind/django-practical-guide-course-code/tree/templates-13-adding-css-styling)
- https://docs.djangoproject.com/en/4.2/ref/templates/
- https://docs.djangoproject.com/en/4.2/topics/templates/

## 33. Module Introduction

- https://docs.python.org/3/library/pathlib.html
- 
## 35. Template Language

- DTL: Django Template Language

## 37. Filters

- https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference

## 38. Django Visual Studio Extension

- https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django

## Settings

- Add Django apps (Python modules) to `settings.py` to have templates available:

		INSTALLED_APPS = [
		'myapp'
		]
- Create subfolders like `myapp/templates/myapp`.
- Templates to inheritate from should be placed in a predefined path, e.g.

		TEMPLATES = [{
			'DIRS': [
				BASE_DIR / 'templates'
			]
		}]