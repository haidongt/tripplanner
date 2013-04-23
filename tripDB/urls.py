from django.conf.urls import patterns, url

from tripDB import views
urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^search_form',  view='tripDB.views.search_form',name='search_form'),
        url(r'^login/$', 'django.contrib.auth.views.login'),
#        url(r'^login/$', 'tripDB.views.login_user'),
)
