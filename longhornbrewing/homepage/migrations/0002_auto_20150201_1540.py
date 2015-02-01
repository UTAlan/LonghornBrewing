# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slogan',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
