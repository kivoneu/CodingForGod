# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('createDate', models.DateTimeField(verbose_name='date created')),
                ('prayerText', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='PrayerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('prayer', models.ForeignKey(to='HomePrayer.Prayer')),
            ],
        ),
        migrations.CreateModel(
            name='PrayerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('userName', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='prayerlog',
            name='user',
            field=models.ForeignKey(to='HomePrayer.PrayerUser'),
        ),
        migrations.AddField(
            model_name='prayer',
            name='createUser',
            field=models.ForeignKey(to='HomePrayer.PrayerUser'),
        ),
    ]
