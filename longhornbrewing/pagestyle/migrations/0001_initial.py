# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('nav_color', models.CharField(max_length=200, blank=True)),
                ('nav_hover_color', models.CharField(max_length=200, blank=True)),
                ('nav_font', models.CharField(max_length=200, blank=True)),
                ('title_color', models.CharField(max_length=200, blank=True)),
                ('title_font', models.CharField(max_length=200, blank=True)),
                ('title_size', models.IntegerField(default=0)),
                ('slogan_color', models.CharField(max_length=200, blank=True)),
                ('slogan_size', models.IntegerField(default=0)),
                ('header_color', models.CharField(max_length=200, blank=True)),
                ('header_font', models.CharField(max_length=200, blank=True)),
                ('content_color', models.CharField(max_length=200, blank=True)),
                ('content_font', models.CharField(max_length=200, blank=True)),
                ('footer_header_color', models.CharField(max_length=200, blank=True)),
                ('footer_content_color', models.CharField(max_length=200, blank=True)),
                ('border_color', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
