from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from profiles.models import Profile


def Maillist(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')


    return render_to_response('internalmails/internalmail.html', locals(), context_instance=RequestContext(request))