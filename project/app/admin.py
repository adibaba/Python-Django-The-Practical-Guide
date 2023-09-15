from django.contrib import admin
from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'id')


admin.site.register(Bookmark, BookmarkAdmin)
