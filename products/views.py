from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HomeView(request, *args, **kwargs):
    return HttpResponse("<h1>hello world home view</h1>")# html code




