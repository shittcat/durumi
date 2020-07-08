#apitest/urls.py
from django.urls import path
from . import apicodes,views
from .apicodes import MapView

app_name = 'apitest'
urlpatterns = [
        path('',views.IndexView.as_view(),name='index'),
        path('contact/',views.ContactView.as_view(),name='contact'),
        path('formtest/',views.FormView.as_view(),name='formtest'),
        path('testview/',views.testView,name='testview'),
        path("pos/", MapView.Pos, name="Pos"),
        path("map/", MapView.MapView, name="Map"),
    ]
    