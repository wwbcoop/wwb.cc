# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20171027_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='published_date',
        ),
    ]