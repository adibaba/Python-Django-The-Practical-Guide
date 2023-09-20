from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Bookmark


class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmarks"] = Bookmark.objects.all()
        return context


def details(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id)
    return render(request, "app/details.html", {
        'bookmark_id': bookmark.id,
        'bookmark_title': bookmark.title,
        'bookmark_url': bookmark.url,
    })
