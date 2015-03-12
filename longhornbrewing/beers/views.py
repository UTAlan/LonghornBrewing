from django.shortcuts import render_to_response
from django.template import RequestContext
from beers.models import Beer, OurBeer

def index(request):
    info = {}

    info['ourbeer'] = OurBeer.objects.get(id=1)
    
    info['beers'] = Beer.objects.all()

    return render_to_response('beers/index.html', { 'info': info }, context_instance=RequestContext(request))
