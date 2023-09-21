from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .models import Bookmark
from .forms import BookmarkForm
from django.http import HttpResponseRedirect


class IndexView(ListView):
    template_name = 'app/index.html'
    model = Bookmark
    context_object_name = "bookmarks"


class BookmarkDetailView(DetailView):
    template_name = 'app/details.html'
    model = Bookmark


class BookmarkFormlView(FormView):
    form_class = BookmarkForm
    template_name = 'app/form.html'
    success_url = '/'

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
