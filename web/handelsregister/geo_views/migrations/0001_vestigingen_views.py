# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from geo_views import migrate


class Migration(migrations.Migration):
    dependencies = [
        ('hr', '__first__'),
    ]

    operations = [

        migrate.ManageView(
            view_name="hr_betrokken_personen",
            sql="""
SELECT row_number() OVER (ORDER BY (( SELECT 1))) AS id,
   mac.naam AS mac_naam,
   mac.kvk_nummer,
   mac.datum_aanvang,
   mac.datum_einde,
   vs.id AS vestiging_id,
   vs.vestigingsnummer,
   p1.id AS persoons_id,
   p1.rol,
       CASE
           WHEN p1.naam IS NOT NULL THEN p1.naam
           WHEN p2.naam IS NOT NULL THEN p2.naam
           WHEN np1.geslachtsnaam IS NOT NULL THEN np1.geslachtsnaam
           ELSE NULL::character varying
       END AS naam,
   p1.rechtsvorm,
   fv.functietitel,
   fv.soortbevoegdheid,
   np2.geslachtsnaam AS bevoegde_naam
  FROM hr_maatschappelijkeactiviteit mac
    JOIN hr_vestiging vs ON vs.maatschappelijke_activiteit_id = mac.id
    JOIN hr_persoon p1 ON mac.eigenaar_id = p1.id
    LEFT JOIN
        hr_natuurlijkpersoon np1 ON np1.id::text = p1.natuurlijkpersoon_id::text
    LEFT JOIN
        hr_functievervulling fv ON fv.heeft_aansprakelijke_id = mac.eigenaar_id
    LEFT JOIN
        hr_persoon p2 ON fv.is_aansprakelijke_id = p2.id
    LEFT JOIN
        hr_natuurlijkpersoon np2 ON np2.id::text = p2.natuurlijkpersoon_id::text
            """),    # noqa
    ]
