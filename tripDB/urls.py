from django.conf.urls import patterns, url

from tripDB import views
urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),

)
