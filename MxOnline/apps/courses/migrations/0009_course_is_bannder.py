# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-23 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20170721_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_bannder',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6e\u64ad'),
        ),
    ]