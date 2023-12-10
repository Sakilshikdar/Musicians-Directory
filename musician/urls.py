from .import views
from django.shortcuts import path

from django.urls import path
urlpatterns=[
    path('',views.musicianhome)
]