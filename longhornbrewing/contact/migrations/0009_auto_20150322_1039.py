# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20150322_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='content_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='business_hours',
            field=tinymce.models.HTMLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='tour_hours',
            field=tinymce.models.HTMLField(blank=True),
            preserve_default=True,
        ),
    ]
