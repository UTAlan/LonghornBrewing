# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_homepage_title_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='footer_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='footer_header_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
