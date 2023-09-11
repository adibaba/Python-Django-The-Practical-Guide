from django.urls import path
from . import views


urlpatterns = [
    # 44. Including Partial Template Snippets
    path('', views.index, name='index'),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='month-challenge')
]
