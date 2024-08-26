from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(resquet):
    return HttpResponse("<h1>soy el index de la app3, cristian vejar</h1>")