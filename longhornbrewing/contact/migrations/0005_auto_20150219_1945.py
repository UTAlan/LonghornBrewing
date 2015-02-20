# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contactpage_title_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='slogan',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='slogan_size',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
