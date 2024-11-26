from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def gwagon(request):
    return HttpResponse('<marquee><h1>Its a Gwagon</h1></marquee>')