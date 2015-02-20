# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20150219_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='map_image',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
