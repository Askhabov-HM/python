from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('health/', health),
    path('categories/', categories),
    path('about/', about),
]