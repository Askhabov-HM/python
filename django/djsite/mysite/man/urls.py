import imp
from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('main/', main)
]