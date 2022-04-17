from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('index page of this site')

def main(request):
    return HttpResponse('main page of this site')