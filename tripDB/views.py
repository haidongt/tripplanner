from django.http import HttpResponse
from django.shortcuts import render_to_response

from django import forms
from django.template import RequestContext
from ajax_select.fields import AutoCompleteField

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    dd = {}
    if request.method == 'GET':

        if request.user.is_authenticated():
            dd["authenticated"] = 1
        else:
            dd["authenticated"] = 0
        return render_to_response('planner/index.html', dd)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        return HttpResponseRedirect("/")
        #return render_to_response('planner/index.html')



# Create your views here.


class SearchForm(forms.Form):

    q = AutoCompleteField(
            'destination',
            required=True,
            help_text="Autocomplete will suggest clie about cats, but you can enter anything you like.",
            label="Favorite Clich",
            attrs={'size': 100}
            )

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
