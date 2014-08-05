from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('events.views',
    #url(r'^medicines/', include('medicines.urls')),
    url(r'^$','Eventlist',name='Eventlist'),
    
)
