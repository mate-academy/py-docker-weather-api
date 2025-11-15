import os
import requests

URL_API_SERVICE = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("WEATHER_API_KEY")
CITY = "Paris"
AQI = "no"


def get_weather() -> str:
    response = requests.get(
        URL_API_SERVICE,
        params={
            "key": API_KEY,
            "q": CITY,
            "aqi": AQI
        }
    )
    current_data = response.json().get("current", {})
    current_temp_c = current_data.get("temp_c", "N/A")

    print(f"Current temperature in {CITY}: {current_temp_c}°C")

    return current_temp_c


if __name__ == "__main__":

    get_weather()
