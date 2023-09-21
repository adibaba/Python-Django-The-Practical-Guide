from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:bookmark_id>', views.details, name='details'),
    path('form/', views.form, name='form'),
]