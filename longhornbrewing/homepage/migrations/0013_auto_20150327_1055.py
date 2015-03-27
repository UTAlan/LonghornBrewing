# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20150324_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='border_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='content_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='footer_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='footer_header_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='header_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='nav_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='nav_hover_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slogan_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slogan_size',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title_color',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title_font',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title_size',
        ),
    ]
