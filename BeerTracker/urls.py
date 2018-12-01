from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('map/', views.map, name='map'),
    #path('getMapData/', views.getFak, name="getMap")
    ]
