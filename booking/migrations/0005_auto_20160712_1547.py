# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-12 12:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20160712_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 12, 12, 47, 4, 393000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 12, 12, 47, 4, 393000, tzinfo=utc)),
        ),
    ]
