import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

URL = "http://api.weatherapi.com/v1/current.json"
# URL for getting current weather, for other services check endpoints on
# https://app.swaggerhub.com/apis-docs/WeatherAPI.com/WeatherAPI/1.0.2

LOCATION = "Paris"
# Pass US Zipcode, UK Postcode, Canada Postalcode,
# IP address, Latitude/Longitude (decimal degree) or city name.
# Visit https://www.weatherapi.com/docs/#intro-request to learn more.

LANGUAGE = None
# LANGUAGE = "uk" #//uncomment it if you want to use language localization
# Returns 'condition:text' field in API in the desired language.
# Visit https://www.weatherapi.com/docs/#intro-request to check 'lang-code'.

PARAMS = {
    "q": LOCATION,
    "key": API_KEY
}

if LANGUAGE:
    PARAMS["lang"] = LANGUAGE


def get_weather() -> None:
    if not PARAMS.get("key"):
        raise ValueError("API_KEY environment variable is not set correctly.")
    response = requests.get(URL, params=PARAMS)

    try:
        assert response.status_code == 200
    except AssertionError:
        raise Exception("Bad request")

    data = response.json()

    current_weather = data.get("current")
    location = data.get("location")

    temp_c = current_weather.get("temp_c")
    last_updated = current_weather.get("last_updated")
    weather = current_weather.get("condition")
    weather_condition = weather.get("text")

    city = location.get("name")
    country = location.get("country")

    print(f"Performing request to Weather API for city {city}...")
    print(
        f"{city}/{country} {last_updated} Weather: "
        f"{temp_c} Celsius, {weather_condition}"
    )


if __name__ == "__main__":
    get_weather()
