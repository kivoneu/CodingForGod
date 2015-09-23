from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .forms import AddPrayerForm
from .models import Prayer, PrayerUser

import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login

from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa

from example.app.decorators import render_to

def addPrayer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddPrayerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            prayerUser = PrayerUser.objects.get(pk=1)
            prayerUser.prayer_set.create(prayerText=form.cleaned_data["prayerText"])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponse(Prayer.objects.all())
            return HttpResponseRedirect('/HomePrayer/addPrayer/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddPrayerForm()

    return render(request, 'HomePrayer/addPrayer.html', {'form': form, 'prayerList': Prayer.objects.all()})

class IndexView(generic.ListView):
    template_name = 'HomePrayer/index.html'
    context_object_name = 'prayer_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Prayer.objects.all()

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')


def context(**extra):
    return dict({
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': ' '.join(GooglePlusAuth.DEFAULT_SCOPE),
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)


@render_to('HomePrayer/home.html')
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return context()


@login_required
@render_to('HomePrayer/home.html')
def done(request):
    """Login complete view, displays user data"""
    return context()


@render_to('HomePrayer/home.html')
def validation_sent(request):
    return context(
        validation_sent=True,
        email=request.session.get('email_validation_address')
    )


@render_to('HomePrayer/home.html')
def require_email(request):
    backend = request.session['partial_pipeline']['backend']
    return context(email_required=True, backend=backend)


@psa('social:complete')
def ajax_auth(request, backend):
    if isinstance(request.backend, BaseOAuth1):
        token = {
            'oauth_token': request.REQUEST.get('access_token'),
            'oauth_token_secret': request.REQUEST.get('access_token_secret'),
        }
    elif isinstance(request.backend, BaseOAuth2):
        token = request.REQUEST.get('access_token')
    else:
        raise HttpResponseBadRequest('Wrong backend type')
    user = request.backend.do_auth(token, ajax=True)
    login(request, user)
    data = {'id': user.id, 'username': user.username}
    return HttpResponse(json.dumps(data), mimetype='application/json')
