from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.main, name = 'main'),
    path('Pos', views.Pos, name='Pos'),
    path('Map', views.MapView, name='Map'),
    path('SimpleMap', views.SimpleMap, name='SimpleMap'),
    #path('example' , views.example, name='example'),
]