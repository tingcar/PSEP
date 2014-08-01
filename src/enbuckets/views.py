from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from profiles.models import Profile
from .models import Enbuck
from internalmail.models import InternalMail

def enbucket(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')
    enbuckets = Enbuck.objects.filter(user=request.user).order_by('entime')
    for enbucket in enbuckets:
    	enbucket.strtime = enbucket.entime.strftime("%Y,%m,%d,%H,%M")

    return render_to_response('enbuckets/enbucket.html', locals(), context_instance=RequestContext(request))