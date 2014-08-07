from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from profiles.models import Profile
from .models import Event
from internalmail.models import InternalMail

def Eventlist(request):

    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')

    events = Event.objects.all()

    return render_to_response('events/singleevent.html', locals(), context_instance=RequestContext(request))