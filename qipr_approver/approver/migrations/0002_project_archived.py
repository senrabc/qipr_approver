# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-24 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
