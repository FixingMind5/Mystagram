"""URL'S modules of platzigram"""

from django.urls import path
from django.http import HttpResponse


def hola_mundo(request):
    """Returns a greeting"""
    return HttpResponse("Hola mundo")

urlpatterns = [
    path('hello', hola_mundo)
]
