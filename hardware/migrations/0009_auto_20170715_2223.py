# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0008_advanced_gw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hard_model',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ustr',
            name='password',
            field=models.CharField(max_length=32, verbose_name='Пароль'),
        ),
    ]
