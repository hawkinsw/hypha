# Generated by Django 2.2.16 on 2020-09-16 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_add_investments_table_and_partners_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnerpage',
            name='name',
        ),
    ]