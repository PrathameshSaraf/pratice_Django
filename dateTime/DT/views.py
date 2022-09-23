from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
x=datetime.now();

def showDT(request):
    return HttpResponse(x);

