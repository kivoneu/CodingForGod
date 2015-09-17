from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .forms import AddPrayerForm
from .models import Prayer, PrayerUser


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


