from django.shortcuts import render_to_response
from django.template import RequestContext
from findus.models import FindUs, Location

def index(request):
    info = {}

    info['locations'] = OurBeer.objects.get(public='true')

    return render_to_response('findus/index.html', { }, context_instance=RequestContext(request))
