from django.shortcuts import render, get_object_or_404
from .models import Bookmark
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect, HttpRequest
from .forms import BookmarkForm
from .models import Bookmark
from django.views import View


def index(request):
    return render(request, "app/index.html", {
        'bookmarks': Bookmark.objects.all(),
        'content': mark_safe('<a href="form/">Form</a>'),
    })


def details(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id)
    return render(request, "app/details.html", {
        'bookmark_id': bookmark.id,
        'bookmark_title': bookmark.title,
        'bookmark_url': bookmark.url,
    })


class BookmarkFormView(View):
    def get(self, request):
        return render(request, "app/form.html", {
            'form': BookmarkForm()
        })

    def post(self, request):
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "app/form.html", {
                'form': form
            })
