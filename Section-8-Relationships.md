# Section 8: Relationships

## Lectures

### 102. Module Introduction

### 103. Understanding Relationship Types

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/relationships-zz-extra-files/slides/slides.pdf)

### 104. Adding a one-to-many Relation & Migrations

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/161c20d..e99a3ca) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/relationships-01-adding-one-to-many)
- Bookmarks 1:1 relation: [Changes](https://github.com/adibaba/Python-Django-The-Practical-Guide/compare/00e2b1b..83a8a84) and
  [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/section-8-code/project)
  for relationships-01-adding-one-to-many
- https://docs.djangoproject.com/en/4.2/topics/db/models/#many-to-one-relationships
- Swapping in models:  
  `python manage.py shell`  
  `from app.models import Bookmark`  
  `Bookmark.objects.all().delete()`

### 105. Working with Relations in Python Code

- Bookmarks 1:1 relation: [Changes](https://github.com/adibaba/Python-Django-The-Practical-Guide/compare/83a8a84..8d75e68) and
  [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/8d75e687385ad4bd228f73c05b5c0c6eee0c0221/project)
  for relationships-01-adding-one-to-many

```python
from app.models import Bookmark, Author
adrian = Author()
adrian = Author(name='Adrian') 
adrian.save()
benjamin = Author(name='Benjamin')
benjamin.save()
Author.objects.all()[0].name

b = Bookmark(url='https://google.com/', title='Google', author=adrian) 
b.save()

b = Bookmark.objects.get(title='Google') 
b.author.name
```

### 106. Cross Model Queries

- https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
- https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey.related_name

```python
b_by_a = Bookmark.objects.all().filter(author__name='Adrian')  # access name with '__'
Bookmark.objects.all().filter(author__name__contains='dri')

a = Author.objects.get(name='Adrian')
a.bookmark_set.all()  # '_set'

from app.models import Bookmark, Author
a = Author.objects.get(name='Adrian')
a.bookmarks.all()  # with related_name in model
```

### 107. Managing Relations in Admin

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/e99a3ca..c48da88) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/relationships-02-managing-relations-in-admin)
  for relationships-02-managing-relations-in-admin

### 108. Adding a one-to-one Relation

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/c48da88..2d4332c) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/relationships-03-adding-one-to-one)
  for relationships-03-adding-one-to-one

### 109. One-to-one Python Code

### 110. One-to-one & Admin Config

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/2d4332c..4db79c4) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/relationships-04-managing-one-to-one-in-admin)
  for relationships-04-managing-one-to-one-in-admin

### 111. Setting-up many-to-many

### 112. Using many-to-many in Python

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/4db79c4..466868f) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/relationships-05-many-to-many)
  for relationships-05-many-to-many

### 113. Many-to-many in Admin

### 114. Circular Relations & Lazy Relations

### 115. Summary

### 116. Useful Resources & Links

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/relationships-zz-extra-files/slides/slides.pdf)

