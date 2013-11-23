from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext as RC

def index(request):
    return render_to_response(
        'index.html',
        {},
        context_instance=RC(request))