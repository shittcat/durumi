# apitest/urls.py
from django.urls import path

from . import views
from .Views import MapView


app_name = 'durumiApp'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='main'),
    path("Pos/", MapView.Pos, name="Pos"),
    path("Map/", MapView.MapView, name="Map"),
    path("Map/tripnote/", MapView.Tripnote, name="tripnote"),
    path("Map/hamburgerMenu/", MapView.HamburgerMenu, name="hamburgerMenu"),
    path("Map/placeView/", MapView.PlaceView, name="placeView"),
    path("Map/pictureView/", MapView.PictureView, name="pictureView"),
    path('firebase-messaging-sw.js',
         views.ServiceWorkerView.as_view(), name='service_worker'),

]
