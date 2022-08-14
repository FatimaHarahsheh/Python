from django.urls import path     
from . import views
urlpatterns = [
    path('', views.anythings),
    path('shows', views.index), #display main page
    path('shows/new',views.diplay), #add new show
    path('addshow',views.addshow), #confirm the add
    path('update/<id>',views.new), #confirm show update
    path('shows/<id>/edit',views.things), #go to edit a show
    path('shows/<id>',views.allinfo), #display all informations
    path('index/<id>',views.destroy),

]



