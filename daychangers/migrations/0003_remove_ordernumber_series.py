# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-31 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daychangers', '0002_auto_20170731_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordernumber',
            name='series',
        ),
    ]
