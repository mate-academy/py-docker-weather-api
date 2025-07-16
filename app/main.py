import os
import requests


CITY = "Kyiv"  # Можеш вказати будь-яке місто
URL = "http://api.weatherapi.com/v1/current.json"  # API для отримання погоди


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Помилка: змінна середовища API_KEY не встановлена.")
        return

    # параметри запиту
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

        print(f"Поточна погода в {CITY}:")
        print(f"Температура: {temp_c}°C")
        print(f"Стан: {condition}")

    except requests.exceptions.HTTPError as r_e:
        print(f"HTTP помилка: {r_e}")
    except Exception as e:
        print(f"Інша помилка: {e}")


if __name__ == "__main__":
    get_weather()
