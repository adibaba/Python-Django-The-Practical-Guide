from django.db import models


class Bookmark(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.url} ({self.title})"
