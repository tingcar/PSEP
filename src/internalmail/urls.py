from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('internalmail.views',
    #url(r'^medicines/', include('medicines.urls')),
    url(r'^$','Maillist',name='Maillist'),
    url(r'^outmail/$','Outmail',name='outmail'),
    url(r'^compose/$','Compose',name='compose'),
    url(r'^compose/submit$','Submit',name='Submit'),
    url(r'^delete$','Delete',name='Delete'),    
)
