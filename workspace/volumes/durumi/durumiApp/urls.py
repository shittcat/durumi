from django.urls import path

from . import views
from .Views import MapView

app_name = "durumiApp"
urlpatterns = [
    # path("", views.main, name="main"),
    path("Pos", MapView.Pos, name="Pos"),
    path("Map", MapView.MapView, name="Map"),
    # path("SimpleMap", views.SimpleMap, name="SimpleMap"),
    # path('example' , views.example, name='example'),
]
