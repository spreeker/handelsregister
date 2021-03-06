# Python
import json
import string
import random
# Packages
from rest_framework.test import APITestCase
from django.core.management import call_command

# Project
from datasets.hr.tests import factories
from handelsregister.tests import authorization
from search import build_index


import logging

log = logging.getLogger(__name__)


class SearchTest(APITestCase, authorization.AuthorizationSetup):

    def setUp(self):
        self.setUpAuthorization()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        hnd1 = factories.Handelsnaam(handelsnaam='handelsnaam1')
        hnd11 = factories.Handelsnaam(handelsnaam='handelsnaam11')
        hnd2 = factories.Handelsnaam(handelsnaam='handelsnaam2')
        hnd3 = factories.Handelsnaam(handelsnaam='handelsnaam3')
        hnd_mac = factories.Handelsnaam(handelsnaam='handelsnaammac')

        onderneming = factories.Onderneming(handelsnamen=[hnd_mac])

        cls.mac1 = factories.MaatschappelijkeActiviteitFactory(
                naam='mac1',
                kvk_nummer='11111111',
                onderneming=onderneming
        )

        cls.mac2 = factories.MaatschappelijkeActiviteitFactory(
                naam='mac2',
                kvk_nummer='01123456'

        )
        cls.mac3 = factories.MaatschappelijkeActiviteitFactory(
                naam='mac3',
                kvk_nummer='01123567'
        )

        cls.ves1 = factories.VestigingFactory(
                naam='test1',
                maatschappelijke_activiteit=cls.mac1,
                vestigingsnummer=99999999,
                # handelsnamen=[hnd1, hnd11]
        )

        cls.ves1.handelsnamen.set([hnd1, hnd11])

        cls.ves2 = factories.VestigingFactory(
                naam='test2',
                maatschappelijke_activiteit=cls.mac2,
                vestigingsnummer=99999899,
                # handelsnamen=[hnd2]
        )
        cls.ves2.handelsnamen.set([hnd2])

        cls.ves3 = factories.VestigingFactory(
                naam='test3',
                maatschappelijke_activiteit=cls.mac3,
                vestigingsnummer=99988999,
                # handelsnamen=[hnd3]

        )

        cls.ves3.handelsnamen.set([hnd3])

        cls.ves00 = factories.VestigingFactory(
                naam='test00',
                maatschappelijke_activiteit=cls.mac3,
                vestigingsnummer='00006123456',
                # handelsnamen=[hnd3]
        )
        cls.ves00.handelsnamen.set([hnd3])

        call_command('build_index', '--reset')
        call_command('build_index', '--build')
        # build_index.reset_hr_docs()
        # build_index.index_mac_docs()
        # build_index.index_ves_docs()

    def test_random_shit_endpoints(self):
        """
        random stuff that crashes search / inspired by smoke tests
        """
        search_endpoints = [
            '/handelsregister/typeahead/',
            '/handelsregister/search/inschrijving/',
            '/handelsregister/search/vestiging/',
            '/handelsregister/search/maatschappelijkeactiviteit/',
            '/handelsregister/geosearch/',
        ]

        for url in search_endpoints:
            log.debug('random_testing: %s', url)
            self.bomb_endpoint(url)

    def bomb_endpoint(self, url):
        """
        Bomb enpoints with junk make sure nothing causes a
        crash
        """

        source = string.ascii_letters + string.digits + ' ' * 20

        for i in range(10):
            key_len = random.randint(1, 35)
            keylist = [random.choice(source) for i in range(key_len)]
            query = "".join(keylist)

            self.client.credentials(
                HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
            response = self.client.get(url, {
                'q': "".join(query)})

            self.assertEqual(response.status_code, 200)

    def test_mac_kvk(self):

        url = '/handelsregister/search/maatschappelijkeactiviteit/'
        query = '01123'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})
        self.assertIn('results', response.data)
        self.assertIn('count', response.data)

        self.assertEqual(response.data['count'], 2)

        query = '0112345'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})
        self.assertEqual(response.data['count'], 1)

        self.assertEqual(response.data['results'][0]['kvk_nummer'], '01123456')

    def test_mac_naam(self):

        url = '/handelsregister/search/maatschappelijkeactiviteit/'
        query = 'mac'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})
        self.assertIn('results', response.data)
        self.assertIn('count', response.data)
        self.assertEqual(response.data['count'], 3)

        query = 'mac3'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})

        # logging.error(json.dumps(response.data['results'], indent=4))

        handelsnamen = [n['naam'] for n in
                        response.data['results'][0]['handelsnamen']]

        self.assertTrue('mac3' in handelsnamen)

    def test_mac_handelsnaam(self):

        url = '/handelsregister/search/maatschappelijkeactiviteit/'

        query = 'handelsnaammac'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})

        self.assertEqual(response.data['count'], 1)
        # logging.error(json.dumps(response.data['results'], indent=4))

        handelsnamen = [n['naam'] for n in
                        response.data['results'][0]['handelsnamen']]

        self.assertTrue('handelsnaammac' in handelsnamen)

    def test_ves_id(self):

        url = '/handelsregister/search/vestiging/'
        query = 99999
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})
        self.assertIn('results', response.data)
        self.assertIn('count', response.data)
        self.assertEqual(response.data['count'], 2)

        query = 999998
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})
        self.assertEqual(response.data['count'], 1)

        self.assertEqual(
            response.data['results'][0]['vestigingsnummer'], '99999899')

    def test_vest_zeros_in_id(self):
        url = '/handelsregister/search/vestiging/'
        query = 61234
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})
        self.assertIn('results', response.data)
        self.assertIn('count', response.data)
        self.assertEqual(response.data['count'], 1)

        self.assertEqual(
            response.data['results'][0]['vestigingsnummer'], '00006123456')

    def test_ves_naam(self):

        url = '/handelsregister/search/vestiging/'
        query = 'test'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})
        self.assertIn('results', response.data)
        self.assertIn('count', response.data)
        self.assertEqual(response.data['count'], 4)

        query = 'test3'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})

        # logging.error(json.dumps(response.data['results'], indent=4))

        handelsnamen = [n['naam'] for n in
                        response.data['results'][0]['handelsnamen']]

        self.assertTrue('test3' in handelsnamen)

    def test_ves_handelsnaam(self):
        url = '/handelsregister/search/vestiging/'
        query = 'handelsnaam3'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'q': query})

        # logging.error(json.dumps(response.data['results'], indent=4))

        handelsnamen = [n['naam'] for n in
                        response.data['results'][0]['handelsnamen']]

        self.assertTrue('handelsnaam3' in handelsnamen)

    def test_geosearch(self):
        url = '/handelsregister/geosearch/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_hr_r))
        response = self.client.get(url, {'item': 'horeca',
                                         'x': 121944,
                                         'y': 487722,
                                         'radius': 100})

        self.assertEqual(response.status_code, 200)
