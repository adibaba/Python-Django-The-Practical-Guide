# Section 12: File Uploads

## Summary

- https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/
- https://docs.djangoproject.com/en/4.2/ref/files/

## Lectures

### 162. Module Introduction

- https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/#basic-file-uploads

### 163. Starting Setup

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/8096580..2b0415d) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/file-upload-00-starting-setup)
  for file-upload-00-starting-setup
- https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.FILES

### 164. Making the File Upload Work

- https://docs.djangoproject.com/en/4.2/ref/files/uploads/

### 165. Storing Uploaded Files Naive Approach

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/2b0415d..0e39713) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/file-upload-01-storing-uploaded-files-naive-approach)
  for file-upload-01-storing-uploaded-files-naive-approach
- https://docs.djangoproject.com/en/4.2/ref/files/uploads/#django.core.files.uploadedfile.UploadedFile.chunks

### 166. Adding a Form with a Filefield

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/0e39713..22faf99) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/file-upload-02-adding-a-form-with-a-filefield)
  for file-upload-02-adding-a-form-with-a-filefield
- https://docs.djangoproject.com/en/4.2/ref/forms/fields/#filefield

### 167. Using Models for File Storage

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/22faf99..42bdffa) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/file-upload-03-using-models-for-file-storage)
  for file-upload-03-using-models-for-file-storage
- https://docs.djangoproject.com/en/4.2/ref/models/fields/#filefield
- https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-MEDIA_ROOT

### 168. Using an Imagefield

- https://docs.djangoproject.com/en/4.2/ref/models/fields/#imagefield
- https://pypi.org/project/Pillow/

### 169. Using a CreateView

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/42bdffa..f0ce8f0) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/file-upload-04-using-a-createview)
  for file-upload-04-using-a-createview
- https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#createview

### 170. Working with the File Field

- https://docs.djangoproject.com/en/4.2/ref/models/fields/#filefield
- https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#listview

### 171. Serving Uploaded Files

- [Changes](https://github.com/adibaba/django-practical-guide-course-code/compare/f0ce8f0..91ceeb1) and
  [Code](https://github.com/adibaba/django-practical-guide-course-code/tree/file-upload-05-serving-uploaded-files)
  for file-upload-05-serving-uploaded-files
- https://docs.djangoproject.com/en/4.2/ref/settings/#media-url
- https://docs.djangoproject.com/en/4.2/ref/urls/#static

### 172. Summary

### 173. Useful Resources & Links