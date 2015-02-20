from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    info = {}

    return render_to_response('contact/index.html', { 'info': info }, context_instance=RequestContext(request))
