# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-04 05:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dosirak', '0014_auto_20160504_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 4, 5, 34, 57, 149738, tzinfo=utc), verbose_name=b'Published Date'),
        ),
    ]