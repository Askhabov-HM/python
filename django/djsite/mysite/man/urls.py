from django.urls import path, re_path


from .views import *

urlpatterns = [
    path('', index, name='man'),
    path('main/', main),
    path('questions/<str:question>/', questions),
    re_path(r'^archive/(?P<yearHere>[0-9]{4})/', archive),
]