# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresources', '0012_auto_20170912_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmatchingresources',
            name='Format',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
