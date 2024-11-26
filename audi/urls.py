from django.urls import path

from audi.views import *

urlpatterns = [
    path('a7/',a7,name='a7'),
]