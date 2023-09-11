# Summary

## Templates

- https://docs.djangoproject.com/en/4.2/ref/templates/
- https://docs.djangoproject.com/en/4.2/topics/templates/
- https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference
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
- Use filters for loops, string manipulation, etc. 