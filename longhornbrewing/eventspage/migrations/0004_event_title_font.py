# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventspage', '0003_event_content_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title_font',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
