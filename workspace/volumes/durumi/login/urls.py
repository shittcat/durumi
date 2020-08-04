#login/ulrs.py
from django.urls import path

from . import views

app_name ='login'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('base/',views.base,name='base'),
    path('loginCheck/',views.loginCheck,name='loginCheck'),
    path('loginOk/',views.loginOk,name='loginOk')
]