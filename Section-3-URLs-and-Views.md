# Section 3: URLs and Views

- [code](00300_monthly_challenges)
- [code official](https://github.com/academind/django-practical-guide-course-code/tree/urls-views-07-practicing-urls-and-views)

## 18. Module Introduction

- URLs (Routes)

## 19. Creating Project

-  (In root folder, added prefix '00300-' afterwards)  
  `python -m django startproject monthly_challenges`
- (In project folder)  
  `python manage.py startapp challenges`
- Command Palette (Ctrl+Shift+P) 'Python: Select Interpreter'
- Command Palette (Ctrl+Shift+P) 'Preferences: Open Workspace Settings (JSON)'  
  (Creates settings.json file)

		{
		"python.languageServer": "Pylance",
		}

## 21. Creating First View and URL

- `python manage.py runserver`
- [http://localhost:8000/challenges/january](http://localhost:8000/challenges/january)