# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0007_ourbeer_title_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourbeer',
            name='content_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ourbeer',
            name='header_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
