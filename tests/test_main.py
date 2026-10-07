import io
import os
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from app.main import get_weather


class GetWeatherTests(unittest.TestCase):
    def test_get_weather_formats_output(self) -> None:
        response = type(
            "FakeResponse",
            (),
            {
                "json": lambda self: {
                    "location": {
                        "name": "Paris",
                        "country": "France",
                        "localtime": "2022-06-14 11:55",
                    },
                    "current": {
                        "temp_c": 22.0,
                        "condition": {"text": "Sunny"},
                    },
                },
                "raise_for_status": lambda self: None,
            },
        )()

        with patch.dict(os.environ, {"API_KEY": "test-key"}, clear=False):
            with patch(
                "app.main.requests.get",
                return_value=response,
            ) as mock_get:
                with io.StringIO() as output_buffer, redirect_stdout(
                    output_buffer
                ):
                    get_weather()
                    printed = output_buffer.getvalue().strip()

        self.assertEqual(
            printed,
            "Paris/France 2022-06-14 11:55 "
            "Weather: 22.0 Celsius, Sunny",
        )
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
