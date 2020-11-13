# apitest/urls.py
from django.urls import path

from . import views
from .Views import mapView, pageView, accountView, tripnoteView, postView

from django.contrib import admin

app_name = 'durumiApp'
urlpatterns = [
    path('', mapView.mapView, name="Map"),
    path("searchKeyword/", mapView.searchKeyword, name="searchKeyword"),
    path("searchLocation/", mapView.searchLocation, name="searchLocation"),
    path("Map/", mapView.mapView, name="Map"),
    path("viewPage/", pageView.viewBase, name="viewBase"),
    path("viewPage/<pageName>/", pageView.viewPage, name="viewPage"),
    path("accountPage/<pageName>/",accountView.select,name="accountPage"),
    path("postPage/<pageName>/", postView.select,name="postPage"),
    path("tripnotePage/<pageName>/",tripnoteView.select,name="tripnotePage"),
    path("selectTripnote", tripnoteView.selectTripnote, name="selectTripnote"),
    path("tripnote", tripnoteView.tripnoteView, name="tripnote"),
    # path("addTripnoteList", tripnoteView.addTripnoteList, name="addTripnoteList"),
    # path("addTripnote", tripnoteView.addTripnote, name="addTripnote"),
    # path("selectTripnoteForaddTripnote", tripnoteView.selectTripnoteForaddTripnote,
        #  name="selectTripnoteForaddTripnote"),
    path("admin/", admin.site.urls),

]
