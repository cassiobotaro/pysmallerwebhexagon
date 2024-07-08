from http import HTTPStatus

from django.test import TestCase
from .models import Rate


class HexagonIndexViewTests(TestCase):
    def setUp(self):
        Rate.objects.create(slug="default", value=1.01).save()

    def test_index_view(self):
        response = self.client.get("/hexagon/default/100/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.assertContains(response, "value = 100")
        self.assertContains(response, "rate = 1.01")
        self.assertContains(response, "result = 101.0")
