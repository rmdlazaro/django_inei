# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-02 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universidad', '0003_auto_20180102_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
