from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('echo/<str:string>', views.echo, name='echo'),
    path('template', views.template, name='template'),
]
