from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from profiles.models import Profile
from internalmail.models import InternalMail


def benchmark(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')


    return render_to_response('benchmark/benchmark.html', locals(), context_instance=RequestContext(request))