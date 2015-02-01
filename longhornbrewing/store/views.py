from django.shortcuts import render_to_response
from django.template import RequestContext
from store.models import Product

def index(request):
    info = {}

    info['products'] = Product.objects.all()

    for product in info['products']:
        product.html_id = product.name.replace(' ', '_').lower()

    return render_to_response('store/index.html', { 'info': info }, context_instance=RequestContext(request))
