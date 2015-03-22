# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventspage', '0002_auto_20150322_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='content_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
