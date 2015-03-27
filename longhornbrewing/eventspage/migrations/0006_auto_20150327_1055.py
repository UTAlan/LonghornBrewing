# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventspage', '0005_event_header_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='content_color',
        ),
        migrations.RemoveField(
            model_name='event',
            name='header_color',
        ),
        migrations.RemoveField(
            model_name='event',
            name='slogan_color',
        ),
        migrations.RemoveField(
            model_name='event',
            name='slogan_size',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title_color',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title_font',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title_size',
        ),
    ]
