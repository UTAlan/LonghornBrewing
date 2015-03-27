# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_store_header_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='content_color',
        ),
        migrations.RemoveField(
            model_name='store',
            name='header_color',
        ),
        migrations.RemoveField(
            model_name='store',
            name='slogan_color',
        ),
        migrations.RemoveField(
            model_name='store',
            name='slogan_size',
        ),
        migrations.RemoveField(
            model_name='store',
            name='title_color',
        ),
        migrations.RemoveField(
            model_name='store',
            name='title_font',
        ),
        migrations.RemoveField(
            model_name='store',
            name='title_size',
        ),
    ]
