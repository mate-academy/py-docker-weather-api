import os
import requests

API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:

    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY") # noqa N806

    if not WEATHER_API_KEY:
        print("❌ WEATHER_API_KEY не знайдений")
        return None

    params = {
        "key": WEATHER_API_KEY,
        "q": CITY,
        "lang": "en"
    }

    try:
        response = requests.get(API_URL, params=params)
        data = response.json()

        if "error" in data:
            print(f"❌ Помилка API: {data['error']['message']}")
            return

        location = data["location"]
        current = data["current"]
        condition = current["condition"]

        print(
            f'{location["name"]}/{location["country"]} '
            f'{location["localtime"]} Weather: '
            f'{current["temp_c"]} Celsius, {condition["text"]}'
        )

    except Exception as e:
        print(f"⚠️ Помилка: {e}")


if __name__ == "__main__":
    get_weather()
