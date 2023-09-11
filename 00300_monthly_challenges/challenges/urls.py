from django.urls import path
from . import views


urlpatterns = [
    # 21.
    # path('index', views.index),

    # 21. / 22.
    # path('january', views.janurary),
    # path('feburary', views.february)

    # 29. Practice
    path('', views.index),

    # 23. Dynamic paths segments
    # 24. Path Converters
    # 27. Reverse Function & Named URLs
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='month-challenge')
]
