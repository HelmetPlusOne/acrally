from django.http import HttpResponse
from django.template import loader

from .models import Track


def index(request):
    tracks = list(Track.objects.order_by("name").values())
    template = loader.get_template('tracks/index.html')
    context = {
        'tracks': tracks,
    }
    return HttpResponse(template.render(context, request))