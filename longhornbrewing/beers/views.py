from django.shortcuts import render_to_response
from django.template import RequestContext
from beers.models import Beer

def index(request):
    info = {}

    info['beers'] = Beer.objects.all()

    return render_to_response('beers/index.html', { 'info': info }, context_instance=RequestContext(request))
