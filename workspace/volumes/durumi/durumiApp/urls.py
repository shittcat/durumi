#apitest/urls.py
from django.urls import path

from . import views
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