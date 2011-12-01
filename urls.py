from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'accident.views.homepage', name='homepage'),
    url(r'^accident/(?P<accident_id>\d+)/$', 'accident.views.detail'), 
    url(r'^accident-types/(?P<accident_id>\d+)/$', 'accident.views.accident_typesdetail'),    
    url(r'^vehicle-types/(?P<vehicle_id>\d+)/$', 'accident.views.vehicle_typesdetail'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
