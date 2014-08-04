from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from profiles.models import Profile
from .models import InternalMail


def Maillist(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')

    internalmails = InternalMail.objects.filter(user=request.user)
    internalmailfirst = InternalMail.objects.filter(user=request.user)[0]
    totalnumber = len(internalmails.filter(is_read=False))
    
    return render_to_response('internalmails/internalmail.html', locals(), context_instance=RequestContext(request))


def Outmail(request):
	try:
		profiles = Profile.objects.get(user=request.user)
		internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
	except:
		return  HttpResponseRedirect('/accounts/login/')

	outmails = InternalMail.objects.filter(From=request.user)
	print outmails

	return render_to_response('internalmails/outmail.html', locals(), context_instance=RequestContext(request))

