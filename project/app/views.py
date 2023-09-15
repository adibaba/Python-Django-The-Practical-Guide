from django.shortcuts import render, get_object_or_404
from .models import Bookmark


def index(request):
    return render(request, "app/index.html", {
        'bookmarks': Bookmark.objects.all(),
    })


def details(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id)
    return render(request, "app/details.html", {
        'bookmark_id': bookmark.id,
        'bookmark_title': bookmark.title,
        'bookmark_url': bookmark.url,
    })
