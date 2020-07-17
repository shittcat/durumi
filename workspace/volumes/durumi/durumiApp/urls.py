#apitest/urls.py
from django.urls import path

from . import views
from .Views import MapView


app_name = 'durumiApp'
urlpatterns = [
        path('',views.IndexView.as_view(),name='main'),
        path("Pos/", MapView.Pos, name="Pos"),
        path("Map/", MapView.MapView, name="Map"),
        path("Map/Tripnote/", MapView.Tripnote, name="Tripnote"),
        path("Map/HamburgerMenu/", MapView.HamburgerMenu, name="HamburgerMenu"),
        path("Map/PlaceView/", MapView.PlaceView, name="PlaceView"),
        path("Map/PictureView/", MapView.PictureView, name="PictureView"),
    ]