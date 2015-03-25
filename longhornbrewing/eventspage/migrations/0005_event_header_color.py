# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventspage', '0004_event_title_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='header_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
