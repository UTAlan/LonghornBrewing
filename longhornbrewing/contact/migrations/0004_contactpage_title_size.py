# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20150201_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='title_size',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
