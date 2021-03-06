# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-04 04:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dosirak', '0013_auto_20160504_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='air',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text4', models.CharField(default=b'\xeb\xb6\x84\xec\x9c\x84\xea\xb8\xb0', max_length=20)),
                ('votes4', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='clean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text5', models.CharField(default=b'\xec\xb2\xad\xea\xb2\xb0\xeb\x8f\x84', max_length=20)),
                ('votes5', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text2', models.CharField(default=b'\xea\xb0\x80\xea\xb2\xa9', max_length=20)),
                ('votes2', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text3', models.CharField(default=b'\xec\x84\x9c\xeb\xb9\x84\xec\x8a\xa4', max_length=20)),
                ('votes3', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='taste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text1', models.CharField(default=b'\xeb\xa7\x9b', max_length=20)),
                ('votes1', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 4, 4, 30, 48, 990544, tzinfo=utc), verbose_name=b'Published Date'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='taste',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosirak.Question'),
        ),
        migrations.AddField(
            model_name='service',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosirak.Question'),
        ),
        migrations.AddField(
            model_name='price',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosirak.Question'),
        ),
        migrations.AddField(
            model_name='clean',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosirak.Question'),
        ),
        migrations.AddField(
            model_name='air',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosirak.Question'),
        ),
    ]
