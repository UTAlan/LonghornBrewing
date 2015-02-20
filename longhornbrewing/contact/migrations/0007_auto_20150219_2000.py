# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20150219_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('title_size', models.IntegerField(default=0)),
                ('slogan', models.CharField(max_length=200, blank=True)),
                ('slogan_size', models.IntegerField(default=0)),
                ('business_hours_title', models.CharField(max_length=200, blank=True)),
                ('business_hours', models.TextField(blank=True)),
                ('tour_hours_title', models.CharField(max_length=200, blank=True)),
                ('tour_hours', models.TextField(blank=True)),
                ('address1', models.CharField(max_length=200, blank=True)),
                ('address2', models.CharField(max_length=200, blank=True)),
                ('phone', models.CharField(max_length=200, blank=True)),
                ('email', models.CharField(max_length=200, blank=True)),
                ('map_title', models.CharField(max_length=200, blank=True)),
                ('map_image', models.ImageField(upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='ContactPage',
        ),
    ]
