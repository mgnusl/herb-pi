# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0009_auto_20160330_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='ideal_ph_max',
            field=models.DecimalField(blank=True, decimal_places=2, default=-1, help_text='Maximum ideal pH value', max_digits=3),
        ),
        migrations.AlterField(
            model_name='plant',
            name='ideal_ph_min',
            field=models.DecimalField(blank=True, decimal_places=2, default=-1, help_text='Minimum ideal pH value', max_digits=3),
        ),
        migrations.AlterField(
            model_name='plant',
            name='shade_tolerance',
            field=models.IntegerField(blank=True, choices=[('NONE', 'NONE'), ('LIGHT', 'LIGHT'), ('PERMANENT', 'PERMANENT')], default=0, help_text='How much shade the plant can tolerate'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='sun_preference',
            field=models.IntegerField(blank=True, choices=[('MINIMAL', 'MINIMAL'), ('FULL', 'FULL')], default=0, help_text='How much sun the plant prefers'),
        ),
    ]