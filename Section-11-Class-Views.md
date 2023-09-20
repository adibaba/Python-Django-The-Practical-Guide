# Section 11: Class Views

## Lectures

### 151. Module Introduction

### 152. Adding Templates

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/1e12bd0..e467fc9) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/class-based-views-01-adding-templates)
  for class-based-views-01-adding-templates

### 153. TemplateView

- Instead of render() you can use TemplateView.
- TemplateView: Renders a given template, with the context containing parameters captured in the URL.
- **template_name** has to contain the template file path.
	- https://github.com/django/django/blob/4.2.5/django/views/generic/base.py#L220
	- https://github.com/django/django/blob/4.2.5/django/views/generic/base.py#L185
- Use **get_context_data()** to provide a configuration dictionary.
  It contains data used in the template.
- [Docs: API Reference ➝ class based views ➝ base ➝  templateview](https://docs.djangoproject.com/en/4.2/ref/class-based-views/base/#templateview)

### 154. Using the TemplateView

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/e467fc9..5bffced) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/class-based-views-02-the-templateview)
  for class-based-views-02-the-templateview
  
### 155. Showing a Detail Template

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/5bffced..2a4ddad) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/class-based-views-03-showing-a-detail-template)
  for class-based-views-03-showing-a-detail-template

### 156. The ListView

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/2a4ddad..3a4a5ab) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/class-based-views-04-the-listview)
  for class-based-views-04-the-listview
- ListView: A page representing a list of objects.
- [Docs: API Reference ➝ class based views ➝ generic display ➝  listview](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#listview)
- Additionally: [Docs: Topics ➝ pagination ➝  paginating a listview](https://docs.djangoproject.com/en/4.2/topics/pagination/#paginating-a-listview)

### 157. DetailView

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/3a4a5ab..3fe50e5) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/class-based-views-05-the-detailview)
  for class-based-views-05-the-detailview
- DetailView: A base view for displaying a single object.
- [Docs: API Reference ➝ class based views ➝ generic display ➝  detailview](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#detailview)

### 158. When to Use Which View

### 159. FormView

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/3fe50e5..cd396dd) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/class-based-views-06-the-formview)
  for class-based-views-06-the-formview
- FormView: A view that displays a form. On error, redisplays the form with validation errors; on success, redirects to a new URL.
- [Docs: API Reference ➝ class based views ➝ generic editing ➝  formview](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#formview)

### 160. CreateView

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/cd396dd..8096580) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/class-based-views-07-the-createview)
  for class-based-views-07-the-createview
- CreateView: A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.
- [Docs: API Reference ➝ class based views ➝ generic editing ➝  createview](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#createview)

### 161. Useful Resources & Links
