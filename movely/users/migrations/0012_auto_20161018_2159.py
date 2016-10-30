# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-18 12:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20161018_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useridealstyle',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 10, 18, 12, 59, 11, 844193, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='UserIdealStyle',
        ),
    ]