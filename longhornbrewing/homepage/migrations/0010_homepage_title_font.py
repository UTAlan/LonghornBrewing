# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_homepage_border_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='title_font',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
