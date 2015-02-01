# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactpage_map_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='business_hours',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='tour_hours',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
