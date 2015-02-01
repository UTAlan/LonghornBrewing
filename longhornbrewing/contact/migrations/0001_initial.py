# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('business_hours_title', models.CharField(max_length=200, blank=True)),
                ('business_hours', models.TextField(max_length=200, blank=True)),
                ('tour_hours', models.TextField(max_length=200, blank=True)),
                ('tour_hours_title', models.CharField(max_length=200, blank=True)),
                ('address1', models.CharField(max_length=200, blank=True)),
                ('address2', models.CharField(max_length=200, blank=True)),
                ('phone', models.CharField(max_length=200, blank=True)),
                ('email', models.CharField(max_length=200, blank=True)),
                ('map_image', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
