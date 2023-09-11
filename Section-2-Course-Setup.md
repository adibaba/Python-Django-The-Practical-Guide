# Section 2: Course Setup

## 9. Installing Python & Django

Notes for Windows 10 and PowerShell.

- Python.exe not executed → Edit path environment variable [StackOverflow](https://stackoverflow.com/a/33180819)
- How to print environment variables to the console in PowerShell? [StackOverflow](https://stackoverflow.com/a/50861113)
- CMD opens Windows Store when I type python → App execution aliases [StackOverflow](https://stackoverflow.com/a/58773979)
- `python -m pip install Django`
- `django-admin` → `python -m django`

## 10. Creating a Django Project

- `python -m django startproject mypage`

## 11. Installing an IDE

- [code.visualstudio.com](https://code.visualstudio.com/)
- Extensions: Python, Pylance
- [Shift]+[Alt]+[F] Format document

## 12. Analyzing the Created Project

- manage.py: CLI tools, e.g. creating database
- \_\_init__.py: Python module
- asgi.py & wsgi.py: Deploy
- settings.py & urls.py: Important

## 13. Starting Development Server

- `python manage.py runserver` → [localhost:8000](http://localhost:8000/)

## 14. Django Apps

- Modules are called Apps
- `python manage.py startapp challenges`

## 15. Analyzing the App

- apps.py: e.g. name
- views.py: Important

## 16. More Advanced Setup Steps

- Virtual environments: https://docs.python.org/3/tutorial/venv.html
- .vscode/settings.json file

		{
		"python.languageServer": "Pylance",
		}