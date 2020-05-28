#apitest/urls.py
from django.urls import path
from . import views 

app_name = 'apitest'
urlpatterns = [
        path('',views.IndexView.as_view(),name='index'),
        path('contact/',views.ContactView.as_view(),name='contact'),
        path('formtest/',views.FormView.as_view(),name='formtest'),
        path('testview/',views.testView,name='testview')
    ]
    