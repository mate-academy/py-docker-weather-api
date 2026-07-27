import os

import requests

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY must be provided")

    try:
        print(f"Requesting weather data for {CITY}...")
        response = requests.get(
            WEATHER_API_URL,
            params={
                "key": api_key,
                "q": CITY,
            },
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        print(f"Failed to get weather data: {error}")
        return

    location = data.get("location", {})
    country = location.get("country", "No country is given")
    city = location.get("name", "No city is given")
    localtime = location.get("localtime", "No localtime is given")

    current = data.get("current", {})
    weather_updated = current.get("last_updated", "No updated date is given")
    temp = current.get("temp_c")

    if temp is None:
        temp = "No temperature is given"
    else:
        temp = f"{temp}°C"

    condition_data = current.get("condition", {})
    condition = condition_data.get("text", "No condition is given")

    print(
        f"📍 {city}, {country}\n"
        f"🕒 Local time: {localtime}\n"
        f"🌦️ Weather updated: {weather_updated}\n"
        f"🌡️ Temperature: {temp}\n"
        f"☁️ Condition: {condition}"
    )


if __name__ == "__main__":
    get_weather()
