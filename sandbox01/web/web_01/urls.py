#App
from django.urls import path
from .views import *

urlpatterns = [
    #path('',test),
    path('',Home,name='Home'),
    path('service/',Service,name='Service'),
]
