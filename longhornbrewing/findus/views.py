from django.shortcuts import render_to_response
from django.template import RequestContext
from findus.models import FindUs

def index(request):
    return render_to_response('findus/index.html', { }, context_instance=RequestContext(request))
