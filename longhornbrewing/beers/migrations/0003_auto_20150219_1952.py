# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0002_ourbeers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OurBeers',
            new_name='OurBeer',
        ),
    ]
