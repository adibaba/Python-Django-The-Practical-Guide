from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Bookmark


class IndexView(ListView):
    template_name = 'app/index.html'
    model = Bookmark
    context_object_name = "bookmarks"


class BookmarkDetailView(DetailView):
    template_name = 'app/details.html'
    model = Bookmark
