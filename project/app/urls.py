from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('details/<int:pk>', views.BookmarkDetailView.as_view(), name='details'),
]
