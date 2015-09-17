from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import AddPrayerForm
from .models import Prayer, PrayerUser

def index(request):
    return HttpResponse("HomePrayer")


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
            return HttpResponse(Prayer.objects.all())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddPrayerForm()

    return render(request, 'HomePrayer/addPrayer.html', {'form': form})


