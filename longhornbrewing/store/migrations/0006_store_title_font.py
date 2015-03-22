# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_store_content_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='title_font',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
