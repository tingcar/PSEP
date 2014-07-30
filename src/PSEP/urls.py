from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    # Examples:
    #static and media
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{
        'document_root': settings.STATIC_ROOT
        }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{
        'document_root': settings.MEDIA_ROOT
        }),
    # url(r'^$', 'PSEP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/',include('registration.backends.default.urls')),

    url(r'^contact/', 'contact.views.contact_us', name='contact_us'),
    url(r'^test/', 'contact.views.test', name='test'),
    url(r'^accounts/dashboard/', 'profiles.views.dashboard',name='dashboard'),
    url(r'^accounts/profile/', include('profiles.urls')),
    url(r'^accounts/enbucket/', include('enbuckets.urls')),
    url(r'^accounts/benchmark/', include('benchmark.urls')),
)
