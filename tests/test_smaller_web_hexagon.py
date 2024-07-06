import unittest

from smallerwebhexagon.smaller_web_hexagon import SmallerWebHexagon, Rater
from smallerwebhexagon.raters import IncodeRater, FileRater
from smallerwebhexagon.starlette_http_adapter import StarletteHttpAdapter
from smallerwebhexagon.fastapi_http_adapter import app as fastapi_adapter
from starlette.testclient import TestClient
from http import HTTPStatus


class TestRequest(unittest.TestCase):
    app: SmallerWebHexagon

    def test_it_works_with_in_code_rater(self):
        self.app = SmallerWebHexagon(IncodeRater())

        self.value_should_produce_rate(100, 1.01)
        self.value_should_produce_rate(200, 1.5)

    def test_it_works_with_file_rater(self):
        self.app = SmallerWebHexagon(FileRater("tests/file_rater.txt"))

        self.value_should_produce_rate(10, 1.0)
        self.value_should_produce_rate(100, 2.0)

    def test_it_runs_via_starlette_adapter(self):
        hex = SmallerWebHexagon(IncodeRater())
        app = StarletteHttpAdapter(hex)

        client = TestClient(app)
        response = client.get("/100")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn("value = 100", response.text)
        self.assertIn("rate = 1.01", response.text)
        self.assertIn("result = 101.0", response.text)

    def test_it_runs_via_fastapi_adapter(self):
        client = TestClient(fastapi_adapter)
        fastapi_adapter.dependency_overrides[Rater] = IncodeRater

        response = client.get("/100")
        json_response = response.json()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(json_response["value"], 100)
        self.assertEqual(json_response["rate"], 1.01)
        self.assertEqual(json_response["result"], 101.0)

    def value_should_produce_rate(self, value: float, expected_rate: float):
        rate, result = self.app.rate_and_result(value)

        self.assertEqual(rate, expected_rate)
        self.assertEqual(result, value * rate)
