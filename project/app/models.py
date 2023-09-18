from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"


class Bookmark(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='bookmarks')

    def __str__(self):
        return f"{self.url} ({self.title})"
