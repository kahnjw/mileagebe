import json

from django.test import TestCase, RequestFactory

from csrf.views import Csrf


class CsrfTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('csrf/url')

    def test_csrf_endpointreturns_token(self):
        response = Csrf.as_view()(self.request)
        response.render()
        self.assertEqual(
            json.loads(response.content), {'csrf_token': 'NOTPROVIDED'})
