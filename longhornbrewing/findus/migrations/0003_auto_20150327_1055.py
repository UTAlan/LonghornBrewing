# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findus', '0002_auto_20150324_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='findus',
            name='slogan_color',
        ),
        migrations.RemoveField(
            model_name='findus',
            name='slogan_size',
        ),
        migrations.RemoveField(
            model_name='findus',
            name='title_color',
        ),
        migrations.RemoveField(
            model_name='findus',
            name='title_font',
        ),
        migrations.RemoveField(
            model_name='findus',
            name='title_size',
        ),
    ]
