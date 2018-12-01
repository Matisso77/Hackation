from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('map/', views.map, name='map'),
    path('shit/', views.shit, name='jsonik')
    #path('getMapData/', views.getFak, name="getMap")
    ]
