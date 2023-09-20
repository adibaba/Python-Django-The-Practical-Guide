# Section 6: Data & Models

## Lectures

### 68. Module Introduction

### 69. Different Kinds of Data

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-zz-extra-files/slides/slides.pdf)

### 70. Understanding Database Options

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-zz-extra-files/slides/slides.pdf)

### 71. Understanding SQL

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-zz-extra-files/slides/slides.pdf)

### 72. Django Models

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-zz-extra-files/slides/slides.pdf)
- [Docs: Topics ➝ db](https://docs.djangoproject.com/en/4.2/topics/db/)

### 73. Creating a Django Model with Fields

- [Docs: Topics ➝ db ➝ models ➝  fields](https://docs.djangoproject.com/en/4.2/topics/db/models/#fields)
- [Docs: API Reference ➝ models ➝ fields ➝  field types](https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types)
- [Docs: API Reference ➝ settings ➝  databases](https://docs.djangoproject.com/en/4.2/ref/settings/#databases)
- [Code:  settings.py](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-01-first-model-and-migration/book_store/settings.py#L77)

### 74. Migrations

- [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/data-models-01-first-model-and-migration)
  for data-models-01-first-model-and-migration
- [Docs: Topics ➝ migrations](https://docs.djangoproject.com/en/4.2/topics/migrations/)
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`

### 75. Inserting Data

- [Docs: API Reference ➝ django admin ➝  shell](https://docs.djangoproject.com/en/4.2/ref/django-admin/#shell)
- [Docs: Topics ➝ db ➝ queries ➝  creating objects](https://docs.djangoproject.com/en/4.2/topics/db/queries/#creating-objects)

### 76. Getting all Entries

- [Docs: Topics ➝ db ➝ queries ➝  retrieving all objects](https://docs.djangoproject.com/en/4.2/topics/db/queries/#retrieving-all-objects)

### 77. Updating Models & Migrations

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/5a3a9f4..4a3cfbd) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/data-models-02-updating-models)
  for data-models-02-updating-models
- [Docs: API Reference ➝ models ➝ instances ➝  str](https://docs.djangoproject.com/en/4.2/ref/models/instances/#str)
- [Docs: API Reference ➝ validators](https://docs.djangoproject.com/en/4.2/ref/validators/)

### 78. Blank vs Null

### 79. Updating Data

- [Docs: Topics ➝ db ➝ queries ➝  saving changes to objects](https://docs.djangoproject.com/en/4.2/topics/db/queries/#saving-changes-to-objects)

### 80. Deleting Data

- [Docs: Topics ➝ db ➝ queries ➝  deleting objects](https://docs.djangoproject.com/en/4.2/topics/db/queries/#deleting-objects)

### 81. Create Instead of Save

- [Docs: API Reference ➝ models ➝ querysets ➝  create](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#create)

### 82. Querying & Filtering Data

- [Docs: Topics ➝ db ➝ queries ➝  field lookups](https://docs.djangoproject.com/en/4.2/topics/db/queries/#field-lookups)
- [Docs: API Reference ➝ models ➝ querysets ➝  field lookups](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups)

### 83. "or" Conditions

- [Docs: Topics ➝ db ➝ queries ➝  complex lookups with q objects](https://docs.djangoproject.com/en/4.2/topics/db/queries/#complex-lookups-with-q-objects)

### 84. Query Performance

- [Docs: Topics ➝ db ➝ queries ➝  chaining filters](https://docs.djangoproject.com/en/4.2/topics/db/queries/#chaining-filters)

### 85. Bulk Operations

- [Docs: Topics ➝ db ➝ queries ➝  deleting objects](https://docs.djangoproject.com/en/4.2/topics/db/queries/#deleting-objects)
- [Docs: Topics ➝ db ➝ optimization ➝  use bulk methods](https://docs.djangoproject.com/en/4.2/topics/db/optimization/#use-bulk-methods)

### 86. Preparing Templates

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/4a3cfbd..4efdf5d) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/data-models-03-preparing-templates)
  for data-models-03-preparing-templates

### 87. Rendering Queried Data in the Template

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/4efdf5d..abe120e) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/data-models-04-rendering-queried-data)
  for data-models-04-rendering-queried-data
	- [Code: models.py](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-04-rendering-queried-data/book_outlet/models.py#L8) defines fields of class
	- [Code: views.py](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-04-rendering-queried-data/book_outlet/views.py#L8) gets all objects
	- [Code: template](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-04-rendering-queried-data/book_outlet/templates/book_outlet/index.html) gets fields to display

### 88. Rendering the Details Page

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/abe120e..5380ae0) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/data-models-05-rendering-the-details-page)
  for data-models-05-rendering-the-details-page
	- [Code: views.py](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-05-rendering-the-details-page/book_outlet/views.py#L15) gets object and sets variables to render
	- [Code: template](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-05-rendering-the-details-page/book_outlet/templates/book_outlet/book_detail.html) uses variables
- [Docs: Topics ➝ http ➝ shortcuts ➝  get object or 404](https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/#get-object-or-404)

### 89. Model URLs

- Code of next lecture
	- [Code: models.py](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-06-using-the-slug-and-updating-field-options/book_outlet/models.py#L19) defines get_absolute_url() to specify URLs for objects
	- [Code: template](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-06-using-the-slug-and-updating-field-options/book_outlet/templates/book_outlet/index.html#L10) uses get_absolute_url
- [Docs: API Reference ➝ models ➝ instances ➝  get absolute url](https://docs.djangoproject.com/en/4.2/ref/models/instances/#get-absolute-url)

### 90. Adding a Slugfield & Overwriting Save

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/5380ae0..81a499c) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/data-models-06-using-the-slug-and-updating-field-options)
  for data-models-06-using-the-slug-and-updating-field-options
  - [Code: models.py](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-06-using-the-slug-and-updating-field-options/book_outlet/models.py#L22) defines slug field and updates it every time an object is saved
- [Docs: API Reference ➝ models ➝ fields ➝  slugfield](https://docs.djangoproject.com/en/4.2/ref/models/fields/#slugfield)

### 91. Using the Slug & Updating Field Options

- Code of last lecture
  - [Code: models.py](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-06-using-the-slug-and-updating-field-options/book_outlet/models.py#L17) as slug field is queried often, `db_index=True` is added
- [Docs: API Reference ➝ models ➝ fields ➝  db index](https://docs.djangoproject.com/en/4.2/ref/models/fields/#db-index)
	- db_index may be deprecated in the future

### 92. Aggregation & Ordering

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/81a499c..8b3bad4) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/data-models-07-aggregation-and-ordering)
  for data-models-07-aggregation-and-ordering
  - [Code: views.py](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-07-aggregation-and-ordering/book_outlet/views.py#L12) uses aggregate(), Avg() and count()

### 93. Summary

### 94. Useful Resources & Links

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/blob/data-models-zz-extra-files/slides/slides.pdf)