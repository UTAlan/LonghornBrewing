# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0004_auto_20150322_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
            preserve_default=True,
        ),
    ]
