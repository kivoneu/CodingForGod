from django.contrib import admin

# Register your models here.
from .models import PrayerUser, Prayer, PrayerLog

admin.site.register(PrayerUser)
admin.site.register(Prayer)
admin.site.register(PrayerLog)
