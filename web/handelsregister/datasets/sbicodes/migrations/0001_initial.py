# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 09:51
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SBICodeHierarchy',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('sbi_tree', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
