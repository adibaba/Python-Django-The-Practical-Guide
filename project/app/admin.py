from django.contrib import admin
from .models import Bookmark, Author, Address, Tag


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'id')


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Tag)
