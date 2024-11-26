from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def m5cs(request):
 return HttpResponse('<h1>its a BMW</h1>')