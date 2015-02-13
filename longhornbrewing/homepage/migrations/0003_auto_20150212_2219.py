# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20150201_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='content',
            new_name='content_left',
        ),
        migrations.AddField(
            model_name='homepage',
            name='content_right',
            field=tinymce.models.HTMLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='slogan_size',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_size',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
