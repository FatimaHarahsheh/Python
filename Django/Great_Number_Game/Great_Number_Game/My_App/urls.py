from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('Test',views.Get_Info),
    path('delete',views.delete)
]
