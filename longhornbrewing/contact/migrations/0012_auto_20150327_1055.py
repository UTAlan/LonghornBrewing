# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_contact_header_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='content_color',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='header_color',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='slogan_color',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='slogan_size',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='title_color',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='title_font',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='title_size',
        ),
    ]
