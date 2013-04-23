from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from tripDB.models import *

#admin.site.register(Destination)
admin.site.register(Route)
admin.site.register(Attraction)

class DestinationAdmin(admin.ModelAdmin):
    form = make_ajax_form(Destination,{'name':'Yellowstone'})
admin.site.register(Destination, DestinationAdmin)
