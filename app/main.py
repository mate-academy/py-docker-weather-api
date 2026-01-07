from dataclasses import dataclass
from typing import Optional
import logging
import sys
import os

from requests.exceptions import (
    RequestException,
    Timeout,
    HTTPError
)
import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

DEFAULT_CITY = "Paris"
AQI_PARAM_KEY = "aqi"
AQI_PARAM_VALUE = "no"


@dataclass
class WeatherData:
    city: str
    country: str
    local_time: str
    temperature_celsius: float
    condition: str

    def __str__(self) -> str:
        return (
            f"{self.city}/{self.country} {self.local_time} "
            f"Weather: {self.temperature_celsius}°C, {self.condition}"
        )


class WeatherAPIError(Exception):
    pass


class WeatherAPIClient:
    BASE_URL = "https://api.weatherapi.com/v1/current.json"
    TIMEOUT = 10

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key must be provided or set in "
                "API_KEY environment variable"
            )

    def get_current_weather(self, city: str) -> WeatherData:
        if not city or not city.strip():
            raise ValueError("City name cannot be empty")

        params = {
            "key": self.api_key,
            "q": city.strip(),
            AQI_PARAM_KEY: AQI_PARAM_VALUE
        }

        try:
            logger.info(f"Fetching weather data for {city}")
            response = requests.get(
                self.BASE_URL,
                params=params,
                timeout=self.TIMEOUT
            )
            response.raise_for_status()

        except Timeout:
            error_msg = f"Request timed out after {self.TIMEOUT} seconds"
            logger.error(error_msg)
            raise WeatherAPIError(error_msg)

        except HTTPError as e:
            error_msg = f"HTTP error occurred: {e.response.status_code}"
            logger.error(error_msg)
            raise WeatherAPIError(error_msg)

        except RequestException as e:
            error_msg = f"Request failed: {str(e)}"
            logger.error(error_msg)
            raise WeatherAPIError(error_msg)

        try:
            data = response.json()
            return self._parse_weather_data(data)

        except (KeyError, ValueError) as e:
            error_msg = f"Failed to parse API response: {str(e)}"
            logger.error(error_msg)
            raise WeatherAPIError(error_msg)

    def _parse_weather_data(self, data: dict) -> WeatherData:
        return WeatherData(
            city=data["location"]["name"],
            country=data["location"]["country"],
            local_time=data["location"]["localtime"],
            temperature_celsius=data["current"]["temp_c"],
            condition=data["current"]["condition"]["text"]
        )


def main() -> None:
    try:
        client = WeatherAPIClient()

        city = os.getenv("WEATHER_CITY", DEFAULT_CITY)
        weather = client.get_current_weather(city)

        print(weather)
        logger.info("Weather data retrieved successfully")

    except ValueError as e:
        logger.error(f"Configuration error: {e}")

    except WeatherAPIError as e:
        logger.error(f"Weather API error: {e}")

    except Exception as e:
        logger.exception(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    sys.exit(main())
