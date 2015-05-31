# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagestyle', '0002_pagestyle_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagestyle',
            name='slogan_font',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
