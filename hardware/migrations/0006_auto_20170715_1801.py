# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 13:01
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0005_auto_20170715_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ustr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=16)),
                ('mask', models.CharField(max_length=16)),
                ('login', models.CharField(default='admin', max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('config', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/storage/configs'), upload_to='')),
                ('hard_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.Types')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.Hard_Model')),
                ('toch_dost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.Toch_dost')),
            ],
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='hard_type',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='model',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='toch_dost',
        ),
        migrations.DeleteModel(
            name='Hardware',
        ),
    ]