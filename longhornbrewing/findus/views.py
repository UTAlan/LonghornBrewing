from django.shortcuts import render_to_response
from django.template import RequestContext
from findus.models import FindUs, Location

def index(request):
    info = {}

    info['locations'] = Location.objects.filter(public=True)

    return render_to_response('findus/index.html', { 'info': info }, context_instance=RequestContext(request))
