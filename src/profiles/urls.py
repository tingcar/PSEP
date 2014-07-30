from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('profiles.views',
    #url(r'^medicines/', include('medicines.urls')),
    url(r'^update$','updateprofile',name='updateprofile'),   
    url(r'^submit$','submitcontact',name='submitcontact'),
    url(r'^$','userprofile',name='userprofile'),
    
)
