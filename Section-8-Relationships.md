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

```python
class Author(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
```

### 109. One-to-one Python Code

```python
from app.models import Author, Address, Bookmark
addr1 = Address(city='Berlin')
addr1.save()
addr2 = Address(city='New York') 
addr2.save()
a = Author.objects.get(name='Adrian')
a.address = addr1
a.save()
b = Author.objects.get(name='Benjamin')
b.address = addr2
b.save()
b.address.city
```

### 110. One-to-one & Admin Config

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/2d4332c..4db79c4) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/relationships-04-managing-one-to-one-in-admin)
  for relationships-04-managing-one-to-one-in-adminFF
- https://docs.djangoproject.com/en/4.2/ref/models/options/#verbose-name-plural

### 111. Setting-up many-to-many

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/4db79c4..466868f) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/relationships-05-many-to-many)
  for relationships-05-many-to-many
- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/relationships-zz-extra-files/slides/slides.pdf)

### 112. Using many-to-many in Python

```python
from app.models import Tag, Bookmark
t_g = Tag(name='german')
t_g.save()
t_e = Tag(name='english')
t_e.save()

Bookmark.objects.all()
g = Bookmark.objects.get(title='Google')
s = Bookmark(url='https://www.sap.com/germany', title='SAP') 
s.save()

g.tags.add(t_e)
g.save()
s.tags.add(t_g)
s.tags.add(t_e) 
s.save()
s.tags.all()
t_e.bookmark_set.all()  # '_set'
```

### 113. Many-to-many in Admin

### 114. Circular Relations & Lazy Relations

- Circular Relations & Lazy Relations
- https://docs.djangoproject.com/en/4.2/ref/models/fields/#module-django.db.models.fields.related

### 115. Summary

### 116. Useful Resources & Links

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/relationships-zz-extra-files/slides/slides.pdf)

