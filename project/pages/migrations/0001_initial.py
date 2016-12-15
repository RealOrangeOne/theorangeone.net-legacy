# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import wagtailmarkdown.blocks
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('wagtailimages', '0015_fill_filter_spec_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('hide_list', models.BooleanField(default=False)),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='SimpleContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('ansi', wagtail.wagtailcore.blocks.TextBlock(template='blocks/ansi.html')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock()), ('gist', wagtail.wagtailcore.blocks.CharBlock(icon='code', template='blocks/gist.html')), ('heading', wagtail.wagtailcore.blocks.StructBlock((('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('value', wagtail.wagtailcore.blocks.CharBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('markdown', wagtailmarkdown.blocks.MarkdownBlock()), ('ol', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='List Item'), icon='list-ol', label='Ordered List', template='blocks/ordered-list.html')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(label='Raw HTML')), ('secret', wagtail.wagtailcore.blocks.RichTextBlock(icon='password', template='blocks/secret.html')), ('ul', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='List Item'), icon='list-ul', label='Unordered List')), ('video', wagtail.wagtailcore.blocks.StructBlock((('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock()))))))),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]
