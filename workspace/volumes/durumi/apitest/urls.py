#apitest/urls.py
from django.urls import path
from . import views
from .apicodes import MapView


app_name = 'apitest'
urlpatterns = [
        path('',views.IndexView.as_view(),name='index'),
        path('contact/',views.ContactView.as_view(),name='contact'),
        path('formtest/',views.FormView.as_view(),name='formtest'),
        path('testview/',views.testView,name='testview'),
        path("Pos/", MapView.Pos, name="Pos"),
        path("Map/", MapView.MapView, name="Map"),
        path("Map/Tripnote/", MapView.Tripnote, name="Tripnote"),
        path("Map/HamburgerMenu/", MapView.HamburgerMenu, name="HamburgerMenu"),
        path("Map/PlaceView/", MapView.PlaceView, name="PlaceView"),
        path("Map/PictureView/", MapView.PictureView, name="PictureView"),
    ]