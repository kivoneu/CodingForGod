from django.db import models

# Create your models here.
class PrayerUser(models.Model):
    userName = models.CharField(max_length=64)

    def __str__(self):
        return self.userName

class Prayer(models.Model):
    createDate = models.DateTimeField('date created')
    createUser = models.ForeignKey(PrayerUser)
    prayerText = models.CharField(max_length=1024)

    def __str__(self):
        return self.prayerText

class PrayerLog(models.Model):
    prayer = models.ForeignKey(Prayer)
    user = models.ForeignKey(PrayerUser)
