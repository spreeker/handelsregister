# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-01 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('hr', '0018_auto_20170105_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbs_sbi_hoofdcat',
            name='hoofdcategorie',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cbs_sbi_subcat',
            name='subcategorie',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cbs_sbicodes',
            name='sub_sub_categorie',
            field=models.CharField(max_length=255),
        ),
    ]
