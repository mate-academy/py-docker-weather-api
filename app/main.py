import os
import requests
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = os.getenv("CITY", "Paris")


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        logging.error("API_KEY environment variable is not set")
        raise ValueError("API_KEY environment variable is required")

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=5)
        response.raise_for_status()

        weather_data = response.json()
        current = weather_data["current"]

        print(f"Current weather in {CITY}:")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Condition: {current['condition']['text']}")

    except requests.exceptions.Timeout:
        logging.error("Request timed out. The server may be down or too slow.")
    except requests.exceptions.ConnectionError:
        logging.error("Network error. Please check your internet connection.")
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(
            f"An error occurred while fetching weather data: {req_err}"
        )
    except KeyError:
        logging.error("Unexpected response structure from Weather API.")


if __name__ == "__main__":
    get_weather()
