# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-03 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosirak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='location',
            field=models.CharField(default=b'\xeb\x8f\x84\xec\x8b\x9c\xeb\x9d\xbd\xec\xa7\x91 \xec\x9c\x84\xec\xb9\x98', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='telephone',
            field=models.CharField(default=b'\xeb\x8f\x84\xec\x8b\x9c\xeb\x9d\xbd\xec\xa7\x91 \xec\x97\xb0\xeb\x9d\xbd\xec\xb2\x98', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=b'\xed\x86\xb5\xec\x9d\xb8\xec\x8b\x9c\xec\x9e\xa5 \xeb\x8f\x84\xec\x8b\x9c\xeb\x9d\xbd\xec\xa7\x91 \xec\x9d\xb4\xeb\xa6\x84', max_length=200),
        ),
    ]