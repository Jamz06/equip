# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0003_auto_20170715_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toch_dost',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.Region', verbose_name='Регион'),
        ),
    ]
