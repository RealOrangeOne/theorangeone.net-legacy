# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 19:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20161216_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionindexpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='simplecontentpage',
            name='image',
        ),
    ]