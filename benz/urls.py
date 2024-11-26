from django.urls import path

from benz.views import *

urlpatterns=[
    path('gwagon/',gwagon,name='gwagon'),
            ]