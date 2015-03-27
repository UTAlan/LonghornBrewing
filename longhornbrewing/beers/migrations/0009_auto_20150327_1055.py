# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0008_auto_20150324_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourbeer',
            name='content_color',
        ),
        migrations.RemoveField(
            model_name='ourbeer',
            name='header_color',
        ),
        migrations.RemoveField(
            model_name='ourbeer',
            name='slogan_color',
        ),
        migrations.RemoveField(
            model_name='ourbeer',
            name='slogan_size',
        ),
        migrations.RemoveField(
            model_name='ourbeer',
            name='title_color',
        ),
        migrations.RemoveField(
            model_name='ourbeer',
            name='title_font',
        ),
        migrations.RemoveField(
            model_name='ourbeer',
            name='title_size',
        ),
    ]
