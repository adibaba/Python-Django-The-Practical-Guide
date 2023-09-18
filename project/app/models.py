from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)


class Bookmark(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.url} ({self.title})"
