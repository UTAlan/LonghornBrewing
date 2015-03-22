# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20150322_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='border_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
