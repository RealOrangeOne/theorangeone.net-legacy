# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 17:43
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_homepage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
    ]
