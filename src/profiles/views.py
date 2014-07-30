from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from contact.models import Contact
from PSEP.utils import id_generator

def dashboard(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')
    print request.user.password
    return render_to_response('dashboard.html', locals(), context_instance=RequestContext(request))

#update the content of userprofile
def updateprofile(request):
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')
    
    profiles.English_name=request.POST['English_name']
    profiles.Chinese_name=request.POST['Chinese_name']
    profiles.Phone_number=request.POST['Phone_number']
    profiles.Distription=request.POST['Distription']
    profiles.Address=request.POST['Address']
    profiles.Email=request.POST['Email']
    try:
        profiles.image = request.POST['image']
    except:
        pass
    profiles.save()
    
    return  HttpResponseRedirect('/accounts/dashboard/')

#get the userprofile
def userprofile(request):
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')
    print request.POST
    return render_to_response('profiles/editprofile.html', locals(), context_instance=RequestContext(request))

#change password

#submit contact form
def submitcontact(request):
    try:
        profiles = Profile.objects.get(user=request.user)
    except:
        return  HttpResponseRedirect('/accounts/login/')

    iid = id_generator() + id_generator()
    contacts = Contact()
    print request.POST
    contacts.full_name = request.POST['full_name']
    contacts.organization = request.POST['organization']
    contacts.email = request.POST['email']
    contacts.message = request.POST['message']
    print request.POST['message']
    contacts.iid = iid
    print request.POST
    contacts.save()

    return render_to_response('profiles/editprofile.html', locals(), context_instance=RequestContext(request))

