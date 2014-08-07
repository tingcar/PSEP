from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from contact.models import Contact
from PSEP.utils import id_generator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from internalmail.models import InternalMail
from events.models import Event

def dashboard(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')

    events = Event.objects.all()
    
    return render_to_response('dashboard.html', locals(), context_instance=RequestContext(request))

#update the content of userprofile
def updateprofile(request):
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
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
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')
    
    return render_to_response('profiles/editprofile.html', locals(), context_instance=RequestContext(request))

#change password

#submit contact form
def submitcontact(request):
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')

    iid = id_generator() + id_generator()
    contacts = Contact()
    contacts.full_name = request.POST['full_name']
    contacts.organization = request.POST['organization']
    contacts.email = request.POST['email']
    contacts.message = request.POST['message']
    contacts.iid = iid
    contacts.save()

    message = "Your message has been submitted !"
    request.session['message'] = message

    return  HttpResponseRedirect('/accounts/profile/')


def changepassword(request):
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')
    
    if authenticate(username=request.user.username, password=request.POST['oldpassword']):
        if request.POST['newpassword1'] == request.POST['newpassword2']:
            message = "Your password has been changed !"
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(request.POST['newpassword1'])
            u.save()
        else:
            message = "The new passwords entered are inconstant !"
    else: 
        message = "Please enter the correct password !"
    request.session['message'] = message
    return HttpResponseRedirect('/accounts/profile/')   

