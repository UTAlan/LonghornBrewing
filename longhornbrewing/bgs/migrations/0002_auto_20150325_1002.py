# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='image',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='background',
            name='use_image',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
