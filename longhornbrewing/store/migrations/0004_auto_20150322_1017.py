# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='slogan_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='title_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
