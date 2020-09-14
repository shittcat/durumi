# apitest/urls.py
from django.urls import path

from . import views
<<<<<<< HEAD
from .Views import MapView
from .Views import tripnoteView

app_name = 'durumiApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='main'),
    path("Pos/", MapView.Pos, name="Pos"),
    path("Map/", MapView.MapView, name="Map"),
    path("Map/tripnote/", MapView.Tripnote, name="tripnote"),
    path("Map/hamburgerMenu/", MapView.HamburgerMenu, name="hamburgerMenu"),
    path("Map/placeView/", MapView.PlaceView, name="placeView"),
    path("Map/pictureView/", MapView.PictureView, name="pictureView"),
    path("SelectTripnote/", tripnoteView.SelectTripnote, name="SelectTripnote"),
]
=======
from .Views import mapView,pageView,accountView


app_name = 'durumiApp'
urlpatterns = [
        path('',mapView.mapView, name="Map"),
        path("searchKeyword/", mapView.searchKeyword, name="searchKeyword"),
        path("searchLocation/", mapView.searchLocation, name="searchLocation"),
        path("Map/", mapView.mapView, name="Map"),
        path("viewPage/",pageView.viewBase,name="viewBase"),
        path("viewPage/<pageName>/",pageView.viewPage,name="viewPage"),
        path("login",accountView.loginCheck,name="loginCheck"),
        path("signup",accountView.signup,name="signup"),
        path("logout",accountView.logOut,name="logOut"),
    ]
>>>>>>> 48f4589801339f4be8845132a9fa05a69f91db46
