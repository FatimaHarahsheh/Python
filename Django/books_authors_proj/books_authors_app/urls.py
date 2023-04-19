from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook',views.add_book),
    path('/addauthors',views.add_author),
    path('books<id>',views.deti),
    path('author',views.author),
    path('author/<id>',views.author_id),
    

]