# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20150322_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='content_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
