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
    print "another time saved"
    newRoute = Route(destA = start, destB = end, user_id = row[0])
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
    for i in range(len(attractions)):
        tmp.append(attractions[len(attractions)-i-1].name)
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
    userRow = User.objects.filter(username = request.user)
    print "row[0].id" + str(id)
    routes = Route.objects.filter(user_id=userRow[0].id)
    print "seleted routes size is: " + str(len(routes))
    i = 0
    print "view routes" + str(len(routes))
    for route in routes:
        i = i+1;
        attractions = route.attraction_set.all()
        tmp = [route.destA]
        for i in range(len(attractions)):
	        tmp.append(attractions[len(attractions)-i-1].name)
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
