import os
import requests


API_URL: str = "http://api.weatherapi.com/v1/current.json"
CITY: str = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    try:
        result = requests.get(API_URL, params={"key": api_key, "q": CITY})
        result.raise_for_status()
    except requests.RequestException as exc:
        print(f"Error: {exc}")
        return
    data = result.json()
    print(
        f"Weather in {CITY}, "
        f"{data.get('location').get('country')} "
        f"{data.get('current').get('last_updated')}\n"
        f"Condition: {data.get('current').get('condition').get('text')}\n"
        f"Temperature: {data.get('current').get('temp_c')} °C\n"
        f"Wind: {data.get('current').get('wind_kph')} km/h\n"
        f"Humidity: {data.get('current').get('humidity')} %\n"
        f"Cloud: {data.get('current').get('cloud')} %"
    )


if __name__ == "__main__":
    get_weather()
