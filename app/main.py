import os
import requests


def get_weather() -> None:
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("Error: WEATHER_API_KEY env variable is not set.")
        return

    url = (
        f"http: //api.weatherapi.com/v1/"
        f"current.json?key={api_key}&q=Kyiv&aqi=no"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location = data.get("location", {}).get("name", "Kyiv")
        temp_c = data.get("current", {}).get("temp_c", "N/A")
        condition = (data.get("current", {}).get
                     ("condition", {}).get("text", "N/A"))

        print(f"Current weather in {location}: {temp_c}°C, {condition}")
    except requests.RequestException as e:
        print("Failed to get weather data:", e)


if __name__ == "__main__":
    get_weather()
