# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-06 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='materia_p',
        ),
        migrations.AddField(
            model_name='profesor',
            name='materia_p',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Materia'),
            preserve_default=False,
        ),
    ]
