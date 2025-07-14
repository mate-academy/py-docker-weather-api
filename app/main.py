import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Ошибка: переменная окружения API_KEY не установлена.")
        return

    # параметры запроса
    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no"
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {CITY}: ")
        print(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")

    except requests.exceptions.HTTPError as r_e:
        print(f"HTTP Error: {r_e}")
    except Exception as e:
        print(f"Common Error: {e}")


if __name__ == "__main__":
    get_weather()
