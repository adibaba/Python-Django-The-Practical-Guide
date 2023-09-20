from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Bookmark


class IndexView(ListView):
    template_name = 'app/index.html'
    model = Bookmark
    context_object_name = "bookmarks"


def details(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id)
    return render(request, "app/details.html", {
        'bookmark_id': bookmark.id,
        'bookmark_title': bookmark.title,
        'bookmark_url': bookmark.url,
    })
