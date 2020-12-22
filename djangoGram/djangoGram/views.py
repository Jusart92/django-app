"""Views"""
# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""

    return HttpResponse('Oh, hi! Current server timi is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))


def sorted_numbers(request):
    """Return a JSON response with sorted integers"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }

    return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 18:
        message = 'Sorry, {nombre}, Not allow here!'.format(nombre=name)
    else:
        message = 'Hello {nombre}! Welcome to Gram'.format(nombre=name)

    return HttpResponse(message)