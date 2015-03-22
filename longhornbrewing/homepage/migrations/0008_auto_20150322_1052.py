# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20150322_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='nav_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='nav_hover_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='slider_active_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='slider_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
