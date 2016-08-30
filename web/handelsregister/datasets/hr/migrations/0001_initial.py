# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-30 13:00
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activiteit',
            fields=[
                ('id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('activiteitsomschrijving', models.TextField(blank=True, help_text='\n            De omschrijving van de activiteiten die de\n            Vestiging of Rechtspersoon uitoefent', null=True)),
                ('sbi_code', models.CharField(help_text='De codering van de activiteit conform de SBI2008', max_length=5)),
                ('sbi_omschrijving', models.CharField(help_text='Omschrijving van de activiteit conform de SBI2008', max_length=300)),
                ('hoofdactiviteit', models.BooleanField(help_text='\n            Indicatie die aangeeft welke van de activiteiten de\n            hoofdactiviteit is')),
            ],
        ),
        migrations.CreateModel(
            name='CommercieleVestiging',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('totaal_werkzame_personen', models.IntegerField(blank=True, null=True)),
                ('fulltime_werkzame_personen', models.IntegerField(blank=True, null=True)),
                ('parttime_werkzame_personen', models.IntegerField(blank=True, null=True)),
                ('import_activiteit', models.NullBooleanField()),
                ('export_activiteit', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Communicatiegegevens',
            fields=[
                ('id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('domeinnaam', models.URLField(blank=True, help_text='Het internetadres (URL)', max_length=300, null=True)),
                ('emailadres', models.EmailField(blank=True, help_text='Het e-mailadres waar op de onderneming gemaild kan worden', max_length=200, null=True)),
                ('toegangscode', models.CharField(blank=True, help_text='\n            De internationale toegangscode van het land waarop het nummer\n            (telefoon of fax) betrekking heeft', max_length=10, null=True)),
                ('communicatie_nummer', models.CharField(blank=True, help_text='Nummer is het telefoon- of faxnummer zonder opmaak', max_length=15, null=True)),
                ('soort_communicatie_nummer', models.CharField(blank=True, choices=[('Telefoon', 'Telefoon'), ('Fax', 'Fax')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Functievervulling',
            fields=[
                ('fvvid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('functietitel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Handelsnaam',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('handelsnaam', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kapitaal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Locatie',
            fields=[
                ('id', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('volledig_adres', models.CharField(blank=True, help_text='Samengesteld adres ', max_length=550, null=True)),
                ('toevoeging_adres', models.TextField(blank=True, help_text='Vrije tekst om een Adres nader aan te kunnen duiden', null=True)),
                ('afgeschermd', models.BooleanField(help_text='Geeft aan of het adres afgeschermd is of niet')),
                ('postbus_nummer', models.CharField(blank=True, max_length=10, null=True)),
                ('bag_nummeraanduiding', models.URLField(blank=True, help_text='Link naar de BAG Nummeraanduiding', null=True)),
                ('bag_adresseerbaar_object', models.URLField(blank=True, help_text='Link naar het BAG Adresseerbaar object', null=True)),
                ('straat_huisnummer', models.CharField(blank=True, max_length=220, null=True)),
                ('postcode_woonplaats', models.CharField(blank=True, max_length=220, null=True)),
                ('regio', models.CharField(blank=True, max_length=170, null=True)),
                ('land', models.CharField(blank=True, max_length=50, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=28992)),
            ],
        ),
        migrations.CreateModel(
            name='MaatschappelijkeActiviteit',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('naam', models.CharField(blank=True, help_text='\n            De (statutaire) naam of eerste handelsnaam van de inschrijving', max_length=600, null=True)),
                ('kvk_nummer', models.CharField(blank=True, help_text='\n            Betreft het identificerende gegeven\n            voor de MaatschappelijkeActiviteit, het KvK-nummer', max_length=8, null=True, unique=True)),
                ('datum_aanvang', models.DateField(blank=True, help_text='De datum van aanvang van de MaatschappelijkeActiviteit', max_length=8, null=True)),
                ('datum_einde', models.DateField(blank=True, help_text='\n            De datum van beëindiging van de MaatschappelijkeActiviteit', max_length=8, null=True)),
                ('incidenteel_uitlenen_arbeidskrachten', models.NullBooleanField(help_text="\n            Indicatie die aangeeft of de ondernemer tijdelijk arbeidskrachten\n            ter beschikking stelt en dit niet onderdeel is van zijn\n            'reguliere' activiteiten.")),
                ('non_mailing', models.NullBooleanField(help_text='\n            Indicator die aangeeft of de inschrijving haar adresgegevens\n            beschikbaar stelt voor mailing-doeleinden.')),
                ('activiteiten', models.ManyToManyField(help_text='\n            De SBI-activiteiten van de MaatschappelijkeActiviteit is het totaal\n            van alle SBI-activiteiten die voorkomen bij de\n            MaatschappelijkeActiviteit behorende " NietCommercieleVestigingen\n            en bij de Rechtspersoon', to='hr.Activiteit')),
                ('bezoekadres', models.ForeignKey(blank=True, help_text='bezoekadres', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.Locatie')),
                ('communicatiegegevens', models.ManyToManyField(help_text='Afgeleid van communicatiegegevens van inschrijving', to='hr.Communicatiegegevens')),
            ],
        ),
        migrations.CreateModel(
            name='NietCommercieleVestiging',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ook_genoemd', models.CharField(blank=True, max_length=200, null=True)),
                ('verkorte_naam', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Onderneming',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('totaal_werkzame_personen', models.IntegerField(blank=True, null=True)),
                ('fulltime_werkzame_personen', models.IntegerField(blank=True, null=True)),
                ('parttime_werkzame_personen', models.IntegerField(blank=True, null=True)),
                ('handelsnamen', models.ManyToManyField(to='hr.Handelsnaam')),
            ],
        ),
        migrations.CreateModel(
            name='Persoon',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('rol', models.CharField(blank=True, max_length=14, null=True)),
                ('rechtsvorm', models.CharField(blank=True, max_length=50, null=True)),
                ('uitgebreide_rechtsvorm', models.CharField(blank=True, max_length=240, null=True)),
                ('volledige_naam', models.CharField(blank=True, max_length=240, null=True)),
                ('voornamen', models.CharField(blank=True, max_length=240, null=True)),
                ('typering', models.CharField(blank=True, max_length=50, null=True)),
                ('reden_insolvatie', models.CharField(blank=True, max_length=50, null=True)),
                ('geboortedatum', models.CharField(blank=True, max_length=8, null=True)),
                ('geboorteplaats', models.CharField(blank=True, max_length=240, null=True)),
                ('geboorteland', models.CharField(blank=True, max_length=50, null=True)),
                ('naam', models.CharField(blank=True, max_length=600, null=True)),
                ('geslachtsnaam', models.CharField(blank=True, max_length=240, null=True)),
                ('geslachtsaanduiding', models.CharField(blank=True, max_length=20, null=True)),
                ('datum_aanvang', models.DateField(blank=True, help_text='De datum van aanvang van de MaatschappelijkeActiviteit', max_length=8, null=True)),
                ('datum_einde', models.DateField(blank=True, help_text='\n            De datum van beëindiging van de MaatschappelijkeActiviteit', max_length=8, null=True)),
                ('soort', models.CharField(blank=True, max_length=21, null=True)),
                ('rsin', models.CharField(blank=True, max_length=9, null=True)),
                ('datumuitschrijving', models.DateField(blank=True, help_text='De datum van aanvang van de MaatschappelijkeActiviteit', max_length=8, null=True)),
                ('verkortenaam', models.CharField(blank=True, max_length=60, null=True)),
                ('volledigenaam', models.CharField(blank=True, max_length=240, null=True)),
                ('nummer', models.CharField(blank=True, max_length=15, null=True)),
                ('toegangscode', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RechterlijkeUitspraak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vestiging',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('vestigingsnummer', models.CharField(help_text='Betreft het identificerende gegeven voor de Vestiging', max_length=12, unique=True)),
                ('hoofdvestiging', models.BooleanField()),
                ('naam', models.CharField(blank=True, max_length=200, null=True)),
                ('datum_aanvang', models.DateField(blank=True, help_text='De datum van aanvang van de Vestiging', null=True)),
                ('datum_einde', models.DateField(blank=True, help_text='De datum van beëindiging van de Vestiging', null=True)),
                ('datum_voortzetting', models.DateField(blank=True, help_text='De datum van voortzetting van de Vestiging', null=True)),
                ('activiteiten', models.ManyToManyField(to='hr.Activiteit')),
                ('bezoekadres', models.ForeignKey(blank=True, help_text='bezoekadres', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.Locatie')),
                ('commerciele_vestiging', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.CommercieleVestiging')),
                ('communicatiegegevens', models.ManyToManyField(help_text='Afgeleid van communicatiegegevens van inschrijving', to='hr.Communicatiegegevens')),
                ('handelsnamen', models.ManyToManyField(to='hr.Handelsnaam')),
                ('maatschappelijke_activiteit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vestigingen', to='hr.MaatschappelijkeActiviteit')),
                ('niet_commerciele_vestiging', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.NietCommercieleVestiging')),
                ('postadres', models.ForeignKey(blank=True, help_text='postadres', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.Locatie')),
            ],
        ),
        migrations.AddField(
            model_name='maatschappelijkeactiviteit',
            name='eigenaar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Persoon'),
        ),
        migrations.AddField(
            model_name='maatschappelijkeactiviteit',
            name='hoofdvestiging',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Vestiging'),
        ),
        migrations.AddField(
            model_name='maatschappelijkeactiviteit',
            name='onderneming',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Onderneming'),
        ),
        migrations.AddField(
            model_name='maatschappelijkeactiviteit',
            name='postadres',
            field=models.ForeignKey(blank=True, help_text='postadres', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.Locatie'),
        ),
    ]
