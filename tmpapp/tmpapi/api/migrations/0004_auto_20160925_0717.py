# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160925_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clause',
            name='data_dokonania_wpisu',
            field=models.DateField(null=True),
        ),
    ]