# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresources', '0008_auto_20170215_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='Pressure',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='Sample_Weight',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='Temperature',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
