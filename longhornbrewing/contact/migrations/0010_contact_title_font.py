# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20150322_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='title_font',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
