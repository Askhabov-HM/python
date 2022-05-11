from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> page not found </h1>")

def health(request):
    return HttpResponse("women/health page")

def categories(request):
    return HttpResponse("<h1>women/categories page</h1>")

def about(request):
    return HttpResponse('<h1>Here infor about our site, bitch</h1>')
