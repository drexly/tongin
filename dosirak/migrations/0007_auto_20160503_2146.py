# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-03 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosirak', '0006_auto_20160503_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='telephone',
            field=models.CharField(default=b'\xeb\x8f\x84\xec\x8b\x9c\xeb\x9d\xbd\xec\xa7\x91 \xec\x97\xb0\xeb\x9d\xbd\xec\xb2\x98', max_length=201),
        ),
    ]
