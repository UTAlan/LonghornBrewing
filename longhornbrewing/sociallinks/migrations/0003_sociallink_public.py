# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sociallinks', '0002_sociallink_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
