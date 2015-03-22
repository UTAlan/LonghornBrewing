# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0003_auto_20150219_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourbeer',
            name='slogan_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ourbeer',
            name='title_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
