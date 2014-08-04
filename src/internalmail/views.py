from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from profiles.models import Profile
from .models import InternalMail, OutMail
from PSEP.utils import id_generator
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def Maillist(request):        
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')

    internalmails = InternalMail.objects.filter(user=request.user)
    try:
        internalmailfirst = InternalMail.objects.filter(user=request.user)[0]
    except:
        internalmailfirst = False

    totalnumber = len(internalmails.filter(is_read=False))
    
    return render_to_response('internalmails/internalmail.html', locals(), context_instance=RequestContext(request))


def Outmail(request):
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')

    try:
        outmailfirst = OutMail.objects.filter(From=request.user)[0]
    except:
        outmailfirst = False    

    outmails = OutMail.objects.filter(From=request.user)
    
    return render_to_response('internalmails/outmail.html', locals(), context_instance=RequestContext(request))
    

def Compose(request):
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')
    
    return render_to_response('internalmails/compose.html', locals(), context_instance=RequestContext(request))

def Submit(request):
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')

    try:
        iid1 = id_generator() + id_generator()
        user = User.objects.get(username__exact=request.POST['toname'])
        newmail = InternalMail(user=user)
        newmail.FromEmail = profiles.user.email
        newmail.is_read = False
        newmail.From = profiles.user.username
        newmail.Title = request.POST['Title']
        newmail.Content = request.POST['Content']
        newmail.Ticketid = iid1
        newmail.slug = iid1
        newmail.Address = profiles.Address
        newmail.save()
        iid2 = id_generator() + id_generator()
        outmail = OutMail(user=user)
        outmail.FromEmail = profiles.user.email
        outmail.is_read = False
        outmail.From = profiles.user.username
        outmail.Title = request.POST['Title']
        outmail.Content = request.POST['Content']
        outmail.Ticketid = iid2
        outmail.slug = iid2
        outmail.Address = profiles.Address
        outmail.save()
        request.session['message'] = "New message has been sent !"
    except:
        request.session['message'] = "The message is failed, please check if the user is exiting !"

    return  HttpResponseRedirect('/accounts/internalmail/compose/')

@csrf_exempt
def Delete(request):
    try:
        profiles = Profile.objects.get(user=request.user)
        internalmails_short = InternalMail.objects.filter(user=request.user)[0:3]
    except:
        return  HttpResponseRedirect('/accounts/login/')
    try:
        emailget = InternalMail.objects.get(Ticketid=request.POST['iid'])
        emailget.delete()
    except:
        emailget = OutMail.objects.get(Ticketid=request.POST['iid'])
        emailget.delete()

    return  HttpResponseRedirect('.')

