# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170912_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmatchingresources',
            name='add_resources',
        ),
        migrations.DeleteModel(
            name='editresources',
        ),
        migrations.RemoveField(
            model_name='technologies',
            name='add_matchingresources',
        ),
        migrations.RemoveField(
            model_name='technologies',
            name='add_resources',
        ),
        migrations.DeleteModel(
            name='addmatchingresources',
        ),
        migrations.DeleteModel(
            name='addresources',
        ),
        migrations.DeleteModel(
            name='Technologies',
        ),
    ]
