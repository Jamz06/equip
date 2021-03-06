# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0009_auto_20170715_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_type', models.CharField(choices=[('1', 'PPOE'), ('2', 'Static'), ('3', 'VLAN'), ('4', 'DHCP')], max_length=1)),
                ('details', models.CharField(max_length=255, verbose_name='Настройки подключения')),
                ('ustr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hardware.Ustr', verbose_name='Устройство')),
            ],
            options={
                'verbose_name': 'Тип подключения',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Провайдеры',
                'verbose_name': 'Провайдер',
            },
        ),
    ]
