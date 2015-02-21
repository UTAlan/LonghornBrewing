# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20150219_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('link', models.CharField(max_length=200, blank=True)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
