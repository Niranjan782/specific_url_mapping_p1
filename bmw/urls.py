from django.urls import path

from bmw.views import *

urlpatterns=[
    path('m5cs/',m5cs,name='m5cs'),
]