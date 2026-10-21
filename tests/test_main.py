import io
import os
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import Mock, patch

import requests

from app.main import CITY, REQUEST_TIMEOUT, URL, get_weather


class WeatherTests(unittest.TestCase):
    def setUp(self):
        self.environment = patch.dict(os.environ, {"API_KEY": "test-secret"})
        self.environment.start()
        self.addCleanup(self.environment.stop)
        self.request = patch("app.main.requests.get")
        self.get = self.request.start()
        self.addCleanup(self.request.stop)
        self.response = Mock()
        self.response.json.return_value = {
            "location": {
                "name": "Paris", "country": "France",
                "localtime": "2026-10-21 12:00",
            },
            "current": {"temp_c": 22.0, "condition": {"text": "Sunny"}},
        }
        self.get.return_value = self.response

    def test_success_matches_assignment_output(self):
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertIsNone(get_weather())
        self.assertEqual(output.getvalue(), (
            "Performing request to Weather API for city Paris...\n"
            "Paris/France 2026-10-21 12:00 Weather: 22.0 Celsius, Sunny\n"
        ))
        self.get.assert_called_once_with(
            URL, params={"key": "test-secret", "q": CITY},
            timeout=REQUEST_TIMEOUT,
        )
        self.response.raise_for_status.assert_called_once_with()

    def test_missing_or_blank_key_prevents_request(self):
        for key in (None, "", "   "):
            with self.subTest(key=key):
                os.environ.pop("API_KEY", None)
                if key is not None:
                    os.environ["API_KEY"] = key
                with self.assertRaisesRegex(RuntimeError, "API_KEY"):
                    get_weather()
        self.get.assert_not_called()

    def test_network_errors_do_not_expose_key(self):
        for exception in (requests.Timeout, requests.ConnectionError):
            with self.subTest(exception=exception):
                self.get.side_effect = exception("key=test-secret")
                with self.assertRaisesRegex(RuntimeError, "Unable") as caught:
                    get_weather()
                self.assertNotIn("test-secret", str(caught.exception))

    def test_http_failure_is_checked_before_json(self):
        self.response.raise_for_status.side_effect = requests.HTTPError(
            "key=test-secret"
        )
        with self.assertRaisesRegex(RuntimeError, "Unable"):
            get_weather()
        self.response.json.assert_not_called()

    def test_malformed_payloads(self):
        for payload in ({}, None, [], {"location": None, "current": {}}):
            with self.subTest(payload=payload):
                self.response.json.return_value = payload
                with self.assertRaisesRegex(RuntimeError, "invalid response"):
                    get_weather()

    def test_invalid_json(self):
        self.response.json.side_effect = ValueError("bad json")
        with self.assertRaisesRegex(RuntimeError, "invalid response"):
            get_weather()

    def test_command_line_missing_key(self):
        environment = dict(os.environ)
        environment.pop("API_KEY", None)
        result = subprocess.run(
            [sys.executable, "app/main.py"], env=environment,
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertEqual(
            result.stderr, "Error: Set the API_KEY environment variable.\n"
        )


if __name__ == "__main__":
    unittest.main()
