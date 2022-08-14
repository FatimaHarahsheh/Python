from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('sub',views.turnin),
    path('log',views.display)
]


