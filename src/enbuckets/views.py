from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from profiles.models import Profile
from .models import Enbuck

def enbucket(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')
    enbuckets = Enbuck.objects.filter(user=request.user)
    return render_to_response('enbuckets/enbucket.html', locals(), context_instance=RequestContext(request))