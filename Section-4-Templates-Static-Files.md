# Section 4: Templates & Static Files

## Lectures

### 32. Module Introduction

### 33. Adding & Registering Templates

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/b3a97ef..7f135f5) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-01-adding-and-registering-templates)
  for templates-01-adding-and-registering-templates
- [Docs: Topics ➝ templates ➝  django.template.loader.render_to_string](https://docs.djangoproject.com/en/4.2/topics/templates/#django.template.loader.render_to_string)

### 34. Rendering Templates

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/7f135f5..4d8aa11) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-02-rendering-templates)
  for templates-02-rendering-templates
- [Docs: Topics ➝ http ➝ shortcuts ➝  render](https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/#render)

### 35. Template Language & Variable Interpolation

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/4d8aa11..27c250a) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-03-template-variables-interpolation)
  for templates-03-template-variables-interpolation
- [Docs: Topics ➝ templates ➝  variables](https://docs.djangoproject.com/en/4.2/topics/templates/#variables)
- DTL: Django Template Language

### 36. Exercise Solution

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/27c250a..e59b36b) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-04-exercise-solution)
  for templates-04-exercise-solution

### 37. Filters

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/e59b36b..0b5a4c9) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-05-filters)
  for templates-05-filters
- [Docs: API Reference ➝ templates ➝ builtins ➝  built in filter reference](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference)

### 38. The Django Visual Studio Code Extension

- https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django
- `.vscode/settings.json` (source: video lecture 54 1:47)
		
		{
		    "emmet.includeLanguages": {
		        "django-html": "html"
		    },
		    "files.associations": {
		        "**/*.html": "html",
		        "**/templates/**/*.html": "django-html"
		    }
		}

### 39. Tags & the "for" Tag

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/0b5a4c9..78f1d75) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-06-the-for-tag)
  for templates-06-the-for-tag
- https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#for

### 40. The URL Tag for Dynamic URLs

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/78f1d75..adfb94b) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-07-url-tag-dynamic-urls)
  for templates-07-url-tag-dynamic-urls
- [Docs: API Reference ➝ templates ➝ builtins ➝  url](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#url)

### 41. The "if" Tag for Conditional Content

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/adfb94b..e9a4ceb) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-08-if-tag)
  for templates-08-if-tag
- [Docs: API Reference ➝ templates ➝ builtins ➝  if](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#if)

### 42. Template Inheritance

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/e9a4ceb..56aa17d) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-09-template-inheritance)
  for templates-09-template-inheritance
- [Docs: API Reference ➝ templates ➝ language ➝  template inheritance](https://docs.djangoproject.com/en/4.2/ref/templates/language/#template-inheritance)

### 43. Exercise Solution

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/56aa17d..25e9ab1) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-10-exercise-solution)
  for templates-10-exercise-solution

### 44. Including Partial Template Snippets

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/25e9ab1..4b8476a) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-11-includes)
  for templates-11-includes
- [Docs: API Reference ➝ templates ➝ builtins ➝  include](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#include)

### 45. More on the Django Template Language (DTL)

### 46. 404 Templates

- [Docs: API Reference ➝ views ➝  the 404 page not found view](https://docs.djangoproject.com/en/4.2/ref/views/#the-404-page-not-found-view)
- [Docs: Howto ➝ error reporting ➝  errors](https://docs.djangoproject.com/en/4.2/howto/error-reporting/#errors)
- [Docs: Topics ➝ http ➝ shortcuts ➝  get object or 404](https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/#get-object-or-404)
- [Docs: Intro ➝ tutorial03 ➝  raising a 404 error](https://docs.djangoproject.com/en/4.2/intro/tutorial03/#raising-a-404-error)

### 47. Adding Static Files

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/4b8476a..e4956b0) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-12-adding-static-files)
  for templates-12-adding-static-files
- [Docs: Howto ➝ static files](https://docs.djangoproject.com/en/4.2/howto/static-files/)

### 48. Adding Global Static Files

- [Docs: Howto ➝ static files](https://docs.djangoproject.com/en/4.2/howto/static-files/)

### 49. Adding CSS Styling

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/e4956b0..1ef4b0b) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/templates-13-adding-css-styling)
  for templates-13-adding-css-styling

### 50. Building Static URLs Dynamically

### 51. Summary

### 52. Useful Resources & Links

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/templates-zz-extra-files/slides/slides.pdf)
 
## Summary

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