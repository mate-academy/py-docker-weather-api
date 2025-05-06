import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("API_KEY не знайдено у змінних середовища!")
        return

    url = f"{URL}?key={api_key}&q={CITY}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Погода у {CITY}: {temp_c}°C, {condition}")
    else:
        print("Не вдалося отримати дані про погоду:", response.text)


if __name__ == "__main__":
    get_weather()
