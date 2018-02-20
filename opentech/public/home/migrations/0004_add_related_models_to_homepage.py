# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-20 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0003_homepage_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotedFunds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PromotedLabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='call_to_action',
        ),
        migrations.AddField(
            model_name='promotedlabs',
            name='source_page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='promoted_labs', to='home.HomePage'),
        ),
        migrations.AddField(
            model_name='promotedfunds',
            name='source_page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='promoted_funds', to='home.HomePage'),
        ),
        migrations.AlterUniqueTogether(
            name='promotedlabs',
            unique_together=set([('page',)]),
        ),
        migrations.AlterUniqueTogether(
            name='promotedfunds',
            unique_together=set([('page',)]),
        ),
    ]
