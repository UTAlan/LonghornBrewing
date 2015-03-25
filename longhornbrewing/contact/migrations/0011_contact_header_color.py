# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_contact_title_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='header_color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
