# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20150212_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='slogan_size',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_size',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
