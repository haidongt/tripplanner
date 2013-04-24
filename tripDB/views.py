from django.http import HttpResponse
from django.shortcuts import render_to_response

from django import forms
from django.template import RequestContext
from ajax_select.fields import AutoCompleteField
from tripDB.models import *
from django.utils import simplejson

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf



def index(request):
    dd = {}
    if request.method == 'GET':

        if request.user.is_authenticated():
            dd["authenticated"] = 1
        else:
            dd["authenticated"] = 0
        return render_to_response('planner/index.html', dd)

def register(request):

    dd = {}
    dd.update(csrf(request))

    if request.method == 'GET':
        return render_to_response('registration/registration.html', dd)

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username
        print password
        print 'aaaaaaaaaaaa'
        try:
            user = User.objects.create_user(username, 'lennon@thebeatles.com', password)
            user.save()
        except:
            dd["register_failed"] = 1
            
        dd["registered"] = 1
        return render_to_response('registration/registration.html', dd)

def existingRoutes(request):
    dd = {}
    if request.method == "GET":
        if request.user.is_authenticated():
            dd["authenticated"] = 1
        else:
            dd["authenticated"] = 0
        return render_to_response('planner/routesview.html', dd)

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
    row = User.objects.filter(username = request.user)
    newRoute = Route(destA = start, destB = end, user = row[0])
    newRoute.save()
    a_order = 0
    for attraction in attractions:
        a_order = a_order + 1
        newAttraction = Attraction(route = newRoute, name = attraction, order = a_order)
        newAttraction.save()
    to_json = {}
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

'''
def recommendFor(request, attractions):
    attractions =  attractions.split("__")
    recommendation = "Champaign"
    to_json = {"recommendation":recommendation}
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
'''

def recommendFor(request, attractions):
    attractions =  attractions.split("__")
    recommendations = []
    for attraction in attractions:
        attraction = attraction.split(",")[0]
        currLoc = Destination.objects.filter(name=attraction)[0]
        myTag = currLoc.tag
        location = currLoc.location.split(",")
        myLog = float(location[0])
        myLat = float(location[1])
        recAttractions = Destination.objects.filter(tag = myTag)
        minDist = 100000000000000
         
        for recAttraction in recAttractions:
            recLocation = recAttraction.location.split(",")
            recLog = float(recLocation[0])
            recLat = float(recLocation[1])
            distance = (myLog - recLog)*(myLog - recLog) + (myLat - recLat)*(myLat - recLat)
            if (distance<minDist and recAttraction.name!=attraction):
                    minDist = distance
                    recommendation = recAttraction.name
        recommendations.append(recommendation)   
    print recommendations
    to_json = {"recommendation":recommendations}
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

def getRouteForId(request, r_id):
    route = Route.objects.get(id=r_id)
    attractions = route.attraction_set.order_by("order")
    tmp = [route.destA]
    for i in range(len(attractions)):
        tmp.append(attractions[i].name)
    tmp.append(route.destB)
    to_json = {"data":tmp}
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

def deleteRouteForId(request, r_id):
    route1 = Route.objects.get(id=r_id)
    route1.delete()
    to_json = {}
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

def viewRoutes(request):
    to_json = {}
    #userRow = User.objects.filter(username = request.user)
    routes = Route.objects.filter(user__username = request.user)
    i = 0
    for route in routes:
        i = i+1;
        attractions = route.attraction_set.order_by("order")
        tmp = [route.destA]
        for i in range(len(attractions)):
	        tmp.append(attractions[i].name)
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


from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

'''
def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('planner/search_form.html')
'''


def logout_user(request):
    logout(request)
    return redirect('/')
