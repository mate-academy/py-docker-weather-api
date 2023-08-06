import os
import requests


def get_weather() -> None:
    city = "Paris"
    key = os.environ["API_KEY"]
    url = f"https://api.weatherapi.com/v1/current.json?q={city}"
    headers = {
        "key": key
    }

    result = requests.get(url, headers=headers)

    data = result.json()
    country = data["location"]["country"]
    last_updated = data["current"]["last_updated"]
    temp_c = data["current"]["temp_c"]
    weather_text = data["current"]["condition"]["text"]
    result_string = (f"{city}/{country} {last_updated} "
                     f"Weather: {temp_c} Celsius, {weather_text}")
    print(f"Performing request to Weather API for city {city}...")
    print(result_string)


if __name__ == "__main__":
    get_weather()
