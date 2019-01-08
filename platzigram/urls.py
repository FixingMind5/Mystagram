"""URL'S modules of platzigram"""
from django.urls import path
from platzigram import views


urlpatterns = [
    path('hello', views.hola_mundo),
    path('hi', views.hi)
]
