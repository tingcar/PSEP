from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('benchmark.views',
    #url(r'^medicines/', include('medicines.urls')),
    url(r'^$','benchmark',name='benchmark'),
    
)
