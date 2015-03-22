# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0005_auto_20150322_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='name_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beer',
            name='name_size',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
