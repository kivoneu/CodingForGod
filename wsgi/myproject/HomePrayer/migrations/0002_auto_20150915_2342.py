# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HomePrayer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prayerlog',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 23, 42, 26, 557328, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prayer',
            name='createDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
