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
    # url(r'^tripplanner/', include('tripplanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/lookups/', include(ajax_select_urls)),
)
