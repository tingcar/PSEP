from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('enbuckets.views',
    #url(r'^medicines/', include('medicines.urls')),
    url(r'^$','enbucket',name='enbucket'),
    
)
