# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import project.projects.models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('wagtailimages', '0015_fill_filter_spec_field'),
        ('wagtaildocs', '0007_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('summary', models.CharField(max_length=500)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('project_url', models.URLField(blank=True, validators=[project.projects.models.validate_url])),
                ('download_url', models.URLField(blank=True, validators=[project.projects.models.validate_url])),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
