# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_store_title_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
