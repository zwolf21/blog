# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.TextField(max_length=512),
        ),
    ]
