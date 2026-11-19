import os
import requests
from requests.exceptions import HTTPError, RequestException


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    try:
        api_key = os.environ["API_KEY"]
    except KeyError:
        raise KeyError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no"
    }

    print("Preforming request to Weather API for city Paris...")
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        location = data["location"]
        current = data["current"]

        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} Celsius, "
            f"{current['condition']['text']}"
        )

    except HTTPError as error:
        raise HTTPError(
            f"Weather API HTTP error: {error}"
        ) from error
    except RequestException as error:
        raise RequestException(
            f"Weather API connection error: {error}"
        ) from error
    except ValueError as error:
        raise ValueError(
            "Invalid JSON response from Weather API."
        ) from error


if __name__ == "__main__":
    get_weather()
