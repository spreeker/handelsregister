from rest_framework import serializers
from rest_framework.reverse import reverse

from datapunt_api import rest
from datasets.sbicodes import models as sbimodels

from . import models


class Communicatiegegevens(serializers.ModelSerializer):
    class Meta(object):
        model = models.Communicatiegegevens
        exclude = (
            'id',
        )


class Handelsnaam(serializers.ModelSerializer):
    class Meta(object):
        model = models.Handelsnaam
        exclude = (
            'id',
        )


class Onderneming(serializers.ModelSerializer):
    handelsnamen = Handelsnaam(many=True)

    class Meta(object):
        model = models.Onderneming
        exclude = (
            'id',
        )


class Locatie(serializers.ModelSerializer):
    class Meta(object):
        model = models.Locatie
        exclude = (
            'id',
        )


class LocatieVestiging(serializers.ModelSerializer):

    toevoeging = serializers.SerializerMethodField()

    kvk_adres = serializers.CharField(source='volledig_adres')

    class Meta(object):
        model = models.Locatie
        fields = (
            'plaats',
            'straatnaam',
            'postcode',
            'huisnummer',
            'toevoeging',
            'correctie',
            'kvk_adres',
        )

    def get_toevoeging(self, obj):
        huisnummertoevoeging = ''
        if obj.huisnummertoevoeging:
            huisnummertoevoeging = obj.huisnummertoevoeging

        huisletter = ''
        if obj.huisletter:
            huisletter = obj.huisletter

        return "{}{}".format(huisnummertoevoeging, huisletter)


class CommercieleVestiging(serializers.ModelSerializer):
    class Meta(object):
        model = models.CommercieleVestiging
        exclude = (
            'id',
        )


class NietCommercieleVestiging(serializers.ModelSerializer):
    class Meta(object):
        model = models.NietCommercieleVestiging
        exclude = (
            'id',
        )


class SBICodeHierarchy(serializers.ModelSerializer):

    class Meta(object):
        model = sbimodels.SBICodeHierarchy
        fields = (
            'code',
            'title',
            'sbi_tree',
            'qa_tree',
        )


class Activiteit(serializers.ModelSerializer):
    class Meta(object):
        model = models.Activiteit
        exclude = (
            'id',
        )


class ActiviteitDataselectie(serializers.ModelSerializer):
    sbi_code_tree = SBICodeHierarchy()

    class Meta(object):
        model = models.Activiteit
        fields = (
            'sbi_code',
            'sbi_omschrijving',
            'hoofdactiviteit',
            'sbi_code_tree',
        )


class MaatschappelijkeActiviteit(rest.HALSerializer):
    dataset = 'hr'

    _display = rest.DisplayField()

    class Meta(object):
        model = models.MaatschappelijkeActiviteit
        lookup_field = 'kvk_nummer'

        extra_kwargs = {
            '_links': {'lookup_field': 'kvk_nummer'}
        }

        fields = (
            '_links',
            'kvk_nummer',
            '_display',
        )


class BijzondereRechtsToestand(serializers.ModelSerializer):

    class Meta(object):
        model = models.Persoon

        fields = (
            'faillissement',
            'status',
            'duur',
            'reden_insolvatie',
        )


class MaatschappelijkeActiviteitDetail(rest.HALSerializer):
    dataset = 'hr'

    _display = rest.DisplayField()
    onderneming = Onderneming()
    communicatiegegevens = Communicatiegegevens(many=True)
    postadres = Locatie()
    bezoekadres = Locatie()
    vestigingen = rest.RelatedSummaryField()

    _bijzondere_rechts_toestand = BijzondereRechtsToestand(source='eigenaar')

    activiteiten = Activiteit(many=True)

    class Meta(object):
        model = models.MaatschappelijkeActiviteit
        lookup_field = 'kvk_nummer'

        extra_kwargs = {
            '_links': {'lookup_field': 'kvk_nummer'},
            'hoofdvestiging': {'lookup_field': 'vestigingsnummer'},
        }

        fields = (
            '_links',
            '_display',
            'onderneming',
            'communicatiegegevens',
            'postadres',
            'bezoekadres',
            'vestigingen',
            'naam',
            'kvk_nummer',
            'datum_aanvang',
            'datum_einde',
            'incidenteel_uitlenen_arbeidskrachten',
            'non_mailing',
            'eigenaar_mks_id',
            'eigenaar',
            'hoofdvestiging',
            'activiteiten',
            '_bijzondere_rechts_toestand'
        )


class PersoonDataselectie(serializers.ModelSerializer):
    class Meta(object):
        model = models.Persoon
        fields = (
            'id',
            'naam',
            'volledige_naam',
            'faillissement',
            'status',
            'duur',
            'reden_insolvatie',
            'rechtsvorm'
        )


class MaatschappelijkeActiviteitDataselectie(serializers.ModelSerializer):
    dataset = 'hr-mac'
    eigenaar = PersoonDataselectie(read_only=True)

    postadres = Locatie()
    bezoekadres = Locatie()

    activiteiten = ActiviteitDataselectie(many=True)
    onderneming = Onderneming()

    class Meta(object):
        model = models.MaatschappelijkeActiviteit
        fields = (
            'id',
            'kvk_nummer',
            'datum_aanvang',
            'activiteiten',
            # 'datum_einde',
            'naam',
            'eigenaar',
            'eigenaar_mks_id',
            'non_mailing',
            'postadres',
            'bezoekadres',
            'onderneming',
        )


class MaatschappelijkeActiviteitDataselectieVes(serializers.ModelSerializer):
    eigenaar = PersoonDataselectie(read_only=True)

    class Meta(object):
        model = models.MaatschappelijkeActiviteit
        fields = (
            'kvk_nummer',
            'datum_aanvang',
            'datum_einde',
            'naam',
            'eigenaar',
            'eigenaar_mks_id',
            'non_mailing',
        )


class Persoon(rest.HALSerializer):
    dataset = 'hr-ves'

    _display = rest.DisplayField()

    class Meta(object):
        model = models.Persoon

        fields = (
            '_links',
            'id',
            '_display',
        )


class NatuurlijkPersoon(serializers.ModelSerializer):

    class Meta(object):
        model = models.NatuurlijkPersoon

        exclude = (
            'id',
        )


class NietNatuurlijkPersoon(serializers.ModelSerializer):

    class Meta(object):
        model = models.NietNatuurlijkPersoon

        exclude = (
            'id',
        )


class PersoonDetail(rest.HALSerializer):
    # dataset = 'hr'

    natuurlijkpersoon = NatuurlijkPersoon()
    niet_natuurlijkpersoon = NietNatuurlijkPersoon()

    maatschappelijke_activiteit = serializers.SerializerMethodField()
    heeft_aansprakelijke = rest.RelatedSummaryField()
    is_aansprakelijke = rest.RelatedSummaryField()

    _display = rest.DisplayField()

    bijzondere_rechts_toestand = serializers.SerializerMethodField()

    class Meta(object):
        model = models.Persoon

        fields = (
            'id',
            '_display',
            'natuurlijkpersoon',
            'niet_natuurlijkpersoon',
            'maatschappelijke_activiteit',

            'is_aansprakelijke',
            'heeft_aansprakelijke',

            'rol',
            'rechtsvorm',
            'uitgebreide_rechtsvorm',
            'volledige_naam',
            'typering',
            'datum_aanvang',
            'datum_einde',
            'soort',
            'datumuitschrijving',
            'nummer',
            'toegangscode',
            'bijzondere_rechts_toestand'
        )

    def get_bijzondere_rechts_toestand(self, obj):
        return {
            'faillissement': obj.faillissement,
            'status': obj.status,
            'duur': obj.duur,
            'reden_insolvatie': obj.reden_insolvatie
        }

    def get_maatschappelijke_activiteit(self, obj):
        if obj.rol == 'EIGENAAR':
            mac = models.MaatschappelijkeActiviteit.objects.get(
                eigenaar=obj.id)
            url = reverse(
                'maatschappelijkeactiviteit-detail',
                request=self.context['request'],
                args=[str(mac.kvk_nummer)])
            return url


class Vestiging(rest.HALSerializer):
    dataset = 'hr'

    locatie = LocatieVestiging()

    _display = rest.DisplayField()

    class Meta(object):
        model = models.Vestiging
        lookup_field = 'vestigingsnummer'

        extra_kwargs = {
            '_links': {'lookup_field': 'vestigingsnummer'}
        }

        fields = (
            '_links',
            '_display',
            'naam',
            'locatie',
        )


class VestigingDetail(rest.HALSerializer):
    dataset = 'hr'

    _display = rest.DisplayField()
    commerciele_vestiging = CommercieleVestiging()
    niet_commerciele_vestiging = NietCommercieleVestiging()
    communicatiegegevens = Communicatiegegevens(many=True)
    postadres = Locatie()
    bezoekadres = Locatie()
    activiteiten = Activiteit(many=True)
    handelsnamen = Handelsnaam(many=True)

    # niet volgens stelselpedia. hoort bij eigenaar / persoon
    _bijzondere_rechts_toestand = BijzondereRechtsToestand(
        source='maatschappelijke_activiteit.eigenaar')

    class Meta(object):
        model = models.Vestiging
        lookup_field = 'vestigingsnummer'
        extra_kwargs = {
            '_links': {'lookup_field': 'vestigingsnummer'},
            'maatschappelijke_activiteit': {'lookup_field': 'kvk_nummer'},
        }
        fields = (
            '_links',
            '_display',
            'maatschappelijke_activiteit',
            'vestigingsnummer',
            'hoofdvestiging',
            'naam',
            'datum_aanvang',
            'datum_einde',
            'datum_voortzetting',

            'commerciele_vestiging',
            'niet_commerciele_vestiging',
            'communicatiegegevens',
            'postadres',
            'bezoekadres',
            'activiteiten',
            'handelsnamen',
            '_bijzondere_rechts_toestand'
        )


class VestigingDataselectie(serializers.ModelSerializer):
    dataset = 'hr'

    postadres = Locatie()
    bezoekadres = Locatie()
    maatschappelijke_activiteit = MaatschappelijkeActiviteitDataselectieVes()
    activiteiten = ActiviteitDataselectie(many=True)
    handelsnamen = Handelsnaam(many=True)

    commerciele_vestiging = CommercieleVestiging()

    class Meta(object):
        model = models.Vestiging
        fields = (
            'vestigingsnummer',
            'naam',
            'hoofdvestiging',
            'postadres',
            'bezoekadres',
            'maatschappelijke_activiteit',
            'activiteiten',
            'handelsnamen',
            'commerciele_vestiging',

        )


class Functievervulling(rest.HALSerializer):
    dataset = 'hr'

    _display = rest.DisplayField()

    class Meta(object):
        model = models.Functievervulling

        fields = (
            '_links',
            '_display',
        )


class FunctievervullingDetail(rest.HALSerializer):
    dataset = 'hr'

    _display = rest.DisplayField()

    class Meta(object):
        model = models.Functievervulling
        fields = '__all__'
