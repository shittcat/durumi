from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.main, name = 'main'),
    path('ajax', views.ajax, name='ajax'),
    path('Pos', views.Pos, name='Pos'),

    #path('example' , views.example, name='example'),
]