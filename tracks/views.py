from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Track


def index(request):
    tracks = list(Track.objects.order_by("name").values())
    return JsonResponse(tracks, safe=False, json_dumps_params={'indent': 4})
