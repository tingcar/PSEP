from django.shortcuts import render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def dashboard(request):

    return render_to_response('dashboard.html', locals(), context_instance=RequestContext(request))
    
