# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findus', '0004_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='findus',
            name='map_height',
            field=models.IntegerField(default=400),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='findus',
            name='map_width',
            field=models.IntegerField(default=600),
            preserve_default=True,
        ),
    ]
