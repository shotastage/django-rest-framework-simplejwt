# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-17 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_blacklist', '0003_auto_20171017_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outstandingtoken',
            name='jti_hex',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
