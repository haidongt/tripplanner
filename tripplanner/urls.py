from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

from tripDB import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('tripDB.urls')),
    url(r'^search_form',  view='tripDB.views.search_form',name='search_form'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'tripDB.views.logout_user'),
    url(r'^register/', 'tripDB.views.register'),

#    url(r'^login/$', 'tripDB.views.login_user'),
    # url(r'^tripplanner/', include('tripplanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/lookups/', include(ajax_select_urls)),

	url(r'^saveroute/(?P<route>.*)/$', 'tripDB.views.saveRoute'),
	url(r'^recommendfor/(?P<attractions>.*)/$', 'tripDB.views.recommendFor'),
	url(r'^viewroutes/', 'tripDB.views.viewRoutes'),
	url(r'^existingroutes/', 'tripDB.views.existingRoutes'),
	url(r'^getrouteforid/(?P<r_id>[0-9]*)/$', 'tripDB.views.getRouteForId'),
	url(r'^deleterouteforid/(?P<r_id>[0-9]*)/$', 'tripDB.views.deleteRouteForId'),


)
