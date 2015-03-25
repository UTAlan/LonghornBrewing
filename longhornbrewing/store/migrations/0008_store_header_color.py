# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_store_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='header_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
