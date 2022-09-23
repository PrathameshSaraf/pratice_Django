from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("<h2>Hello Saraf </h2>");