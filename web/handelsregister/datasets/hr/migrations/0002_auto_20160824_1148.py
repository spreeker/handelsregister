# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-24 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handelsnaam',
            name='onderneming',
        ),
        migrations.AddField(
            model_name='onderneming',
            name='handelsnamen',
            field=models.ManyToManyField(to='hr.Handelsnaam'),
        ),
    ]