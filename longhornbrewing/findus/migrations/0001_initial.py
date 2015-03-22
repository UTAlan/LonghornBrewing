# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FindUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('title_size', models.IntegerField(default=0)),
                ('title_color', models.CharField(max_length=200, blank=True)),
                ('title_font', models.CharField(max_length=200, blank=True)),
                ('slogan', models.CharField(max_length=200, blank=True)),
                ('slogan_size', models.IntegerField(default=0)),
                ('slogan_color', models.CharField(max_length=200, blank=True)),
                ('page_content', tinymce.models.HTMLField(blank=True)),
                ('public', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
