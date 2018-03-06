# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-06 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_activity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='visibility',
            field=models.CharField(choices=[('all', 'All'), ('private', 'Internal')], default='all', max_length=10),
        ),
    ]
