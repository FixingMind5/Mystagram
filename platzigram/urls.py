"""URL'S modules of platzigram"""
from django.urls import path
from platzigram import views


urlpatterns = [
    path('hello', views.hola_mundo),
    path('sorted', views.sorted_integers),
    path('hi/<str:name>/<int:age>', views.say_hi)
]
