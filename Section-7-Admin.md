# Section 7: Admin

## Lectures

### 95. Module Introduction

### 96. Logging Data Into the Admin Panel

- https://docs.djangoproject.com/en/4.2/intro/tutorial02/#creating-an-admin-user
- `python manage.py createsuperuser`

### 97. Adding Models to the Admin Area

- https://docs.djangoproject.com/en/4.2/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin

```python
# admin.py

from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

### 98. Configuring Model Fields

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/8b3bad4..9c4a0dd) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/admin-01-configuring-model-fields)
  for admin-01-configuring-model-fields
- add e.g. `blank=True` or `editable=False`
- https://docs.djangoproject.com/en/4.2/ref/models/fields/#editable

### 99. Configuring the Admin Settings

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/9c4a0dd..52a5968) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/admin-02-configuring-the-admin-settings)
  for admin-02-configuring-the-admin-settings
- https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#module-django.contrib.admin

### 100. More Config Options

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/52a5968..161c20d) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/admin-03-more-config-options)
  for admin-03-more-config-options
- https://docs.djangoproject.com/en/4.2/ref/contrib/admin/

### 101. Useful Resources & Links


