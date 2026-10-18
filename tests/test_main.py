import importlib
import io
import os
import unittest
from contextlib import redirect_stdout
from unittest.mock import Mock, patch

import requests

from app import main


class WeatherTests(unittest.TestCase):
    def setUp(self) -> None:
        self.api_key = "weather-test-secret"
        self.environment = patch.dict(
            os.environ, {"API_KEY": self.api_key}, clear=True
        )
        self.environment.start()
        self.addCleanup(self.environment.stop)
        self.response = Mock()
        self.response.json.return_value = {
            "location": {
                "name": "Paris",
                "country": "France",
                "localtime": "2022-06-14 11:55",
            },
            "current": {
                "temp_c": 22.0,
                "condition": {"text": "Sunny"},
            },
        }
        self.request_patch = patch(
            "requests.get", return_value=self.response
        )
        self.request = self.request_patch.start()
        self.addCleanup(self.request_patch.stop)

    def test_prints_current_paris_weather(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            result = main.get_weather()

        self.assertIsNone(result)
        self.request.assert_called_once_with(
            "https://api.weatherapi.com/v1/current.json",
            params={"key": self.api_key, "q": "Paris"},
            timeout=10,
        )
        self.response.raise_for_status.assert_called_once_with()
        self.assertEqual(
            output.getvalue(),
            "Performing request to Weather API for city Paris...\n"
            "Paris/France 2022-06-14 11:55 Weather: "
            "22.0 Celsius, Sunny\n",
        )

    def test_import_without_key_then_read_key_when_called(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            importlib.reload(main)

        self.request.assert_not_called()
        with redirect_stdout(io.StringIO()):
            main.get_weather()

        self.request.assert_called_once_with(
            "https://api.weatherapi.com/v1/current.json",
            params={"key": self.api_key, "q": "Paris"},
            timeout=10,
        )

    def test_missing_or_empty_api_key_exits_before_request(self) -> None:
        for environment in ({}, {"API_KEY": ""}):
            with self.subTest(environment=environment):
                with patch.dict(os.environ, environment, clear=True):
                    with self.assertRaisesRegex(SystemExit, "API_KEY"):
                        main.get_weather()
                self.request.assert_not_called()

    def test_request_failures_do_not_disclose_api_key(self) -> None:
        error_url = (
            "https://api.weatherapi.com/v1/current.json"
            f"?key={self.api_key}&q=Paris"
        )
        for error_type in (requests.Timeout, requests.HTTPError):
            with self.subTest(error_type=error_type.__name__):
                self.request.side_effect = None
                self.response.raise_for_status.side_effect = None
                if error_type is requests.Timeout:
                    self.request.side_effect = error_type(error_url)
                else:
                    self.response.raise_for_status.side_effect = (
                        error_type(error_url)
                    )
                output = io.StringIO()

                with redirect_stdout(output):
                    with self.assertRaises(SystemExit) as caught:
                        main.get_weather()

                self.assertEqual(
                    str(caught.exception),
                    "Unable to retrieve weather from WeatherAPI.",
                )
                self.assertNotIn(
                    self.api_key, output.getvalue() + str(caught.exception)
                )
                self.response.json.assert_not_called()


if __name__ == "__main__":
    unittest.main()