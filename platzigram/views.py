"""platzigram views"""
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime


def hola_mundo(request):
    """Returns a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Hola mundo, Current server time is {now}".format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def hi(request):
    """Just a hi"""
    numbers = sorted(request.GET['numbers'].split(","))
    response = JsonResponse([numbers], safe=False)
    return response
