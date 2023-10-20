import os
import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"

params = {
    "key": API_KEY,
    "q": CITY
}


class WeatherDataRetrievalError(Exception):
    pass


def get_weather() -> None:
    response = requests.get(API_URL, params=params)
    print(f"Performing request to Weather API for city {CITY}...")

    if not API_KEY:
        raise WeatherDataRetrievalError(
            "API_KEY environment variable is not set."
        )

    if response.status_code != 200:
        raise WeatherDataRetrievalError(
            f"Failed to retrieve weather data. Status code:"
            f" {response.status_code}"
        )

    response_data = response.json()

    if "error" in response_data:
        raise WeatherDataRetrievalError(
            f"Error from Weather API: {response_data['error']['message']}"
        )

    location_info = response_data.get("location", {})
    if not location_info:
        print("Location information not found in the response.")
    else:
        weather_info = response_data.get("current", {})
        if not weather_info:
            print("Weather information not found in the response.")
        else:
            print(f"{location_info['name']}/{location_info['country']} "
                  f"{location_info['localtime']} "
                  f"Weather: {weather_info.get('temp_c')} "
                  f"Celsius, "
                  f"{weather_info.get('condition', {}).get('text', '')}")


if __name__ == "__main__":
    try:
        get_weather()
    except WeatherDataRetrievalError as e:
        print(f"An error occurred: {e}")
