# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='estanteria_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.estanteria'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='numerounidades',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='objeto_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.objeto'),
        ),
    ]