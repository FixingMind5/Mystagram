"""platzigram views"""
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Utilities
from datetime import datetime


def hola_mundo(request):
    """Returns a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Hola mundo, Current server time is {now}".format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sorted_integers(request):
    """Return a Json with sorted integers"""
    numbers = sorted(request.GET['numbers'].split(","))
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': "Integers sorted successfully."
    }
    response = JsonResponse(
            [data],
            json_dumps_params = {'indent': 4},
            safe=False
        )
    return response


def say_hi(request, name, age):
    """Return a validation"""
    if age < 12:
        return HttpResponse("Sorry {} your not allowed to use this application".format(name))
    else:
        return HttpResponse("Hello {}, nice to have you here".format(name))
