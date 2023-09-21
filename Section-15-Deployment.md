# Section 15: Deployment

## Lectures

### 202. Module Introduction

### 203. Deployment Considerations

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/tree/deployment-zz-extra-files/slides/slides.pdf)

### 204. Which Database

### 205. Django & Web Servers

[Docs: Howto ➝ deployment](https://docs.djangoproject.com/en/4.2/howto/deployment/)

### 206. Serving Static Files

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/tree/deployment-zz-extra-files/slides/slides.pdf)
- [Docs: Howto ➝ static files ➝ deployment](https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/)

### 207. Choosing a Hosting Provider

### 208. Getting Started & Revisiting Settings

### 209. Collecting Static Files

- [Docs: API Reference ➝ settings ➝  std setting STATIC_ROOT](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STATIC_ROOT)

### 210. Serving Static Files

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/5d174f2..334da0b) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/deployment-01-serving-static-files-with-django)
  for deployment-01-serving-static-files-with-django
- [Docs: API Reference ➝ contrib ➝ staticfiles ➝  collectstatic](https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#collectstatic)

### 211. A Note About Migrations

- [Docs: API Reference ➝ django admin ➝  createsuperuser](https://docs.djangoproject.com/en/4.2/ref/django-admin/#createsuperuser)

### 212. Locking in Dependencies

- `python -m pip freeze > requirements.txt`
- `python -m venv django_my_site`
- https://docs.python.org/3/library/venv.html#creating-virtual-environments

### 213. More on Virtual Environments

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/334da0b..5b77f4a) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/deployment-02-using-environment-variables)
  for deployment-02-using-environment-variables

### 214. Using Environment Variables

### 215. Deploying with Elastic Beanstalk

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/5b77f4a..2db71fe) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/deployment-03-deploying-with-elastic-beanstalk)
  for deployment-03-deploying-with-elastic-beanstalk

### 216. SSL & Custom Domains

### 217. Connecting PostgreSQL

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/2db71fe..652d96c) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/deployment-04-connecting-postgresql)
  for deployment-04-connecting-postgresql

### 218. Serving Static Files Separately

### 219. Serving Static Files via S3

- https://django-storages.readthedocs.io/
- https://aws.amazon.com/sdk-for-python/

### 220. Moving File Uploads to S3

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/652d96c..842391a) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/deployment-05-serving-static-files-and-uploads-via-s3)
  for deployment-05-serving-static-files-and-uploads-via-s3

### 221. Summary

### 222. Useful Resources & Links

- [Slides](https://github.com/adibaba/django-practical-guide-course-code/tree/deployment-zz-extra-files/slides/slides.pdf)
