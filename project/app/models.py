from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}"

    class Meta:
        verbose_name_plural = 'Address Entries'


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
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.url} ({self.title})"
