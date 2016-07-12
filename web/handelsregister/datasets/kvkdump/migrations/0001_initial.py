# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-12 12:35
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kvk_adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adrid', models.DecimalField(decimal_places=0, max_digits=18)),
                ('afgeschermd', models.CharField(blank=True, max_length=3, null=True)),
                ('huisletter', models.CharField(blank=True, max_length=1, null=True)),
                ('huisnummer', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('huisnummertoevoeging', models.CharField(blank=True, max_length=5, null=True)),
                ('identificatieaoa', models.CharField(blank=True, max_length=16, null=True)),
                ('identificatietgo', models.CharField(blank=True, max_length=16, null=True)),
                ('land', models.CharField(blank=True, max_length=50, null=True)),
                ('plaats', models.CharField(blank=True, max_length=100, null=True)),
                ('postbusnummer', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('postcode', models.CharField(blank=True, max_length=6, null=True)),
                ('postcodewoonplaats', models.CharField(blank=True, max_length=220, null=True)),
                ('regio', models.CharField(blank=True, max_length=170, null=True)),
                ('straathuisnummer', models.CharField(blank=True, max_length=220, null=True)),
                ('straatnaam', models.CharField(blank=True, max_length=100, null=True)),
                ('toevoegingadres', models.CharField(blank=True, max_length=100, null=True)),
                ('totenmetadres', models.CharField(blank=True, max_length=3, null=True)),
                ('typering', models.CharField(blank=True, max_length=13, null=True)),
                ('vesid', models.DecimalField(blank=True, decimal_places=0, max_digits=18, null=True)),
                ('macid', models.DecimalField(blank=True, decimal_places=0, max_digits=18, null=True)),
                ('volledigadres', models.CharField(blank=True, max_length=550, null=True)),
                ('xcoordinaat', models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True)),
                ('ycoordinaat', models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True)),
                ('adrhibver', models.DecimalField(decimal_places=0, max_digits=19)),
                ('geopunt', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=28992)),
            ],
            options={
                'db_table': 'kvkadrm00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvk_handelsnaam',
            fields=[
                ('hdnid', models.DecimalField(decimal_places=0, max_digits=18, primary_key=True, serialize=False)),
                ('handelsnaam', models.CharField(blank=True, max_length=700, null=True)),
                ('hdnhibver', models.DecimalField(decimal_places=0, max_digits=19)),
            ],
            options={
                'db_table': 'kvkhdnm00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvk_maatschappelijkeactiviteit',
            fields=[
                ('macid', models.DecimalField(decimal_places=0, max_digits=18, primary_key=True, serialize=False)),
                ('beherendekamer', models.CharField(blank=True, max_length=100, null=True)),
                ('domeinnaam1', models.CharField(blank=True, max_length=300, null=True)),
                ('domeinnaam2', models.CharField(blank=True, max_length=300, null=True)),
                ('domeinnaam3', models.CharField(blank=True, max_length=300, null=True)),
                ('emailadres1', models.CharField(blank=True, max_length=200, null=True)),
                ('emailadres2', models.CharField(blank=True, max_length=200, null=True)),
                ('emailadres3', models.CharField(blank=True, max_length=200, null=True)),
                ('fulltimewerkzamepersonen', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('indicatieonderneming', models.CharField(blank=True, max_length=3, null=True)),
                ('kvknummer', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('naam', models.CharField(blank=True, max_length=600, null=True)),
                ('nonmailing', models.CharField(blank=True, max_length=3, null=True)),
                ('nummer1', models.CharField(blank=True, max_length=15, null=True)),
                ('nummer2', models.CharField(blank=True, max_length=15, null=True)),
                ('nummer3', models.CharField(blank=True, max_length=15, null=True)),
                ('parttimewerkzamepersonen', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('prsid', models.DecimalField(decimal_places=0, max_digits=18)),
                ('soort1', models.CharField(blank=True, max_length=10, null=True)),
                ('soort2', models.CharField(blank=True, max_length=10, null=True)),
                ('soort3', models.CharField(blank=True, max_length=10, null=True)),
                ('toegangscode1', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('toegangscode2', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('toegangscode3', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('totaalwerkzamepersonen', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('datumaanvang', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('datumeinde', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('laatstbijgewerkt', models.DateTimeField()),
                ('statusobject', models.CharField(max_length=20)),
                ('machibver', models.DecimalField(decimal_places=0, max_digits=19)),
            ],
            options={
                'db_table': 'kvkmacm00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvk_vestiging',
            fields=[
                ('vesid', models.DecimalField(decimal_places=0, max_digits=18, primary_key=True, serialize=False)),
                ('datumaanvang', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('datumeinde', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('datumuitschrijving', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('eerstehandelsnaam', models.CharField(blank=True, max_length=600, null=True)),
                ('eindgeldigheidactiviteit', models.DecimalField(blank=True, decimal_places=0, max_digits=17, null=True)),
                ('exportactiviteit', models.CharField(blank=True, max_length=3, null=True)),
                ('fulltimewerkzamepersonen', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('importactiviteit', models.CharField(blank=True, max_length=3, null=True)),
                ('indicatiehoofdvestiging', models.CharField(blank=True, max_length=3, null=True)),
                ('macid', models.DecimalField(decimal_places=0, max_digits=18)),
                ('naam', models.CharField(blank=True, max_length=500, null=True)),
                ('nummer1', models.CharField(blank=True, max_length=15, null=True)),
                ('nummer2', models.CharField(blank=True, max_length=15, null=True)),
                ('nummer3', models.CharField(blank=True, max_length=15, null=True)),
                ('omschrijvingactiviteit', models.CharField(blank=True, max_length=2000, null=True)),
                ('ookgenoemd', models.CharField(blank=True, max_length=600, null=True)),
                ('parttimewerkzamepersonen', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('registratietijdstip', models.DecimalField(blank=True, decimal_places=0, max_digits=17, null=True)),
                ('sbicodehoofdactiviteit', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('sbicodenevenactiviteit1', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('sbicodenevenactiviteit2', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('sbicodenevenactiviteit3', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('sbiomschrijvinghoofdact', models.CharField(blank=True, max_length=180, null=True)),
                ('sbiomschrijvingnevenact1', models.CharField(blank=True, max_length=180, null=True)),
                ('sbiomschrijvingnevenact2', models.CharField(blank=True, max_length=180, null=True)),
                ('sbiomschrijvingnevenact3', models.CharField(blank=True, max_length=180, null=True)),
                ('domeinnaam1', models.CharField(blank=True, max_length=300, null=True)),
                ('domeinnaam2', models.CharField(blank=True, max_length=300, null=True)),
                ('domeinnaam3', models.CharField(blank=True, max_length=300, null=True)),
                ('emailadres1', models.CharField(blank=True, max_length=200, null=True)),
                ('emailadres2', models.CharField(blank=True, max_length=200, null=True)),
                ('emailadres3', models.CharField(blank=True, max_length=200, null=True)),
                ('soort1', models.CharField(blank=True, max_length=10, null=True)),
                ('soort2', models.CharField(blank=True, max_length=10, null=True)),
                ('soort3', models.CharField(blank=True, max_length=10, null=True)),
                ('toegangscode1', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('toegangscode2', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('toegangscode3', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('totaalwerkzamepersonen', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('typeringvestiging', models.CharField(blank=True, max_length=3, null=True)),
                ('verkortenaam', models.CharField(blank=True, max_length=60, null=True)),
                ('vestigingsnummer', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('statusobject', models.CharField(max_length=20)),
                ('veshibver', models.DecimalField(decimal_places=0, max_digits=19)),
            ],
            options={
                'db_table': 'kvkvesm00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvk_vestiging_handelsnaam',
            fields=[
                ('veshdnid', models.DecimalField(decimal_places=0, max_digits=18, primary_key=True, serialize=False)),
                ('hdnid', models.DecimalField(decimal_places=0, max_digits=18)),
                ('vesid', models.DecimalField(decimal_places=0, max_digits=18)),
                ('beginrelatie', models.DecimalField(blank=True, decimal_places=0, max_digits=17, null=True)),
                ('eindrelatie', models.DecimalField(blank=True, decimal_places=0, max_digits=17, null=True)),
                ('veshdnhibver', models.DecimalField(decimal_places=0, max_digits=19)),
            ],
            options={
                'db_table': 'kvkveshdnm00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvkprsashm00',
            fields=[
                ('ashid', models.DecimalField(decimal_places=0, max_digits=18, primary_key=True, serialize=False)),
                ('functie', models.CharField(blank=True, max_length=20, null=True)),
                ('prsidh', models.DecimalField(decimal_places=0, max_digits=18)),
                ('prsidi', models.DecimalField(decimal_places=0, max_digits=18)),
                ('soort', models.CharField(blank=True, max_length=20, null=True)),
                ('prsashhibver', models.DecimalField(decimal_places=0, max_digits=19)),
            ],
            options={
                'db_table': 'kvkprsashm00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvkprsm00',
            fields=[
                ('prsid', models.DecimalField(decimal_places=0, max_digits=18, primary_key=True, serialize=False)),
                ('datumuitschrijving', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('datumuitspraak', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('duur', models.CharField(blank=True, max_length=240, null=True)),
                ('faillissement', models.CharField(blank=True, max_length=3, null=True)),
                ('geboortedatum', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('geboorteland', models.CharField(blank=True, max_length=50, null=True)),
                ('geboorteplaats', models.CharField(blank=True, max_length=240, null=True)),
                ('geemigreerd', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('geheim', models.CharField(blank=True, max_length=3, null=True)),
                ('geslachtsaanduiding', models.CharField(blank=True, max_length=20, null=True)),
                ('geslachtsnaam', models.CharField(blank=True, max_length=240, null=True)),
                ('handlichting', models.CharField(blank=True, max_length=3, null=True)),
                ('huwelijksdatum', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('naam', models.CharField(blank=True, max_length=600, null=True)),
                ('nummer', models.CharField(blank=True, max_length=15, null=True)),
                ('ookgenoemd', models.CharField(blank=True, max_length=600, null=True)),
                ('persoonsrechtsvorm', models.CharField(blank=True, max_length=240, null=True)),
                ('redeninsolvatie', models.CharField(blank=True, max_length=50, null=True)),
                ('rsin', models.CharField(blank=True, max_length=9, null=True)),
                ('soort', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('toegangscode', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('typering', models.CharField(blank=True, max_length=40, null=True)),
                ('uitgebreiderechtsvorm', models.CharField(blank=True, max_length=240, null=True)),
                ('verkortenaam', models.CharField(blank=True, max_length=60, null=True)),
                ('volledigenaam', models.CharField(blank=True, max_length=240, null=True)),
                ('voornamen', models.CharField(blank=True, max_length=240, null=True)),
                ('voorvoegselgeslachtsnaam', models.CharField(blank=True, max_length=15, null=True)),
                ('prshibver', models.DecimalField(decimal_places=0, max_digits=19)),
                ('rechtsvorm', models.CharField(blank=True, max_length=50, null=True)),
                ('doelrechtsvorm', models.CharField(blank=True, max_length=50, null=True)),
                ('rol', models.CharField(blank=True, max_length=14, null=True)),
            ],
            options={
                'db_table': 'kvkprsm00',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvkveshism00',
            fields=[
                ('hisvesid', models.DecimalField(decimal_places=0, max_digits=18, primary_key=True, serialize=False)),
                ('vestigingsnummer', models.CharField(max_length=12)),
                ('kvknummer', models.CharField(max_length=8)),
                ('enddate', models.DecimalField(blank=True, decimal_places=0, max_digits=17, null=True)),
                ('hishibver', models.DecimalField(decimal_places=0, max_digits=19)),
            ],
            options={
                'db_table': 'kvkveshism00',
                'managed': False,
            },
        ),
    ]
