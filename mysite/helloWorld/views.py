from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show(request):
    return HttpResponse('<h1 align="center">Hello World</h1>')