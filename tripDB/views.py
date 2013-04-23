from django.http import HttpResponse
from django.shortcuts import render_to_response

from django import forms
from django.template import RequestContext
from ajax_select.fields import AutoCompleteField
from tripDB.models import *
from django.utils import simplejson


def index(request):
    if request.method == "GET":
        return render_to_response('planner/index.html')


def existingRoutes(request):
    if request.method == "GET":
        return render_to_response('planner/routesview.html')

# Create your views here.


class SearchForm(forms.Form):

    q = AutoCompleteField(
            'destination',
            required=True,
            help_text="Autocomplete will suggest clie about cats, but you can enter anything you like.",
            label="Favorite Clich",
            attrs={'size': 100}
            )
def saveRoute(request, route):
    route =  route.split("__")
    start = route[0]
    end = route[-1]
    attractions = route[1:-1]
    newRoute = Route(destA = start, destB = end)
    newRoute.save()
    for attraction in attractions:
        newAttraction = Attraction(route = newRoute, name = attraction)
        newAttraction.save()

    to_json = {}
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

def getRouteForId(request, r_id):
    route = Route.objects.get(id=r_id)
    attractions = route.attraction_set.all()
    tmp = [route.destA]
    for attraction in attractions:
        tmp.append(attraction.name)
    tmp.append(route.destB)
    to_json = {"data":tmp}
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

def viewRoutes(request):
    to_json = {}
    routes = Route.objects.all()
    i = 0
    print "view routes"
    for route in routes:
        i = i+1;
        attractions = route.attraction_set.all()
        tmp = [route.destA]
        for attraction in attractions:
            tmp.append(attraction.name)
        tmp.append(route.destB)
        to_json[route.id] = tmp
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')


def search_form(request):

    dd = {}
    if 'q' in request.GET:
        dd['entered'] = request.GET.get('q')
    initial = {'q':"\"This is an initial value,\" said O'Leary."}
    form = SearchForm(initial=initial)
    dd['form'] = form
    return render_to_response('planner/search_form.html',dd,context_instance=RequestContext(request))
