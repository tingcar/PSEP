from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile

def dashboard(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')
    return render_to_response('dashboard.html', locals(), context_instance=RequestContext(request))

def updateprofile(request):
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')
    
    profiles.English_name=request.POST['English_name']
    profiles.Chinese_name=request.POST['Chinese_name']
    profiles.Initials=request.POST['Initials']
    profiles.Post=request.POST['Post']
     
    try:
        profiles.image = request.POST['image']
    except:
        pass
    
    profiles.save()
    
    return  HttpResponseRedirect('/accounts/profile/')


def userprofile(request):
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')
    return render_to_response('profiles/editprofile.html', locals(), context_instance=RequestContext(request))


