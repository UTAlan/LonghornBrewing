# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20150324_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='header_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
