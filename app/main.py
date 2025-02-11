import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY is missing!")
        return

    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": "Paris"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Перевірка на HTTP-помилки
        data = response.json()
        weather = data["current"]

        print(
            f'Paris, {data["location"]["country"]} - '
            f'{data["location"]["localtime"]}'
        )
        print(
            f'Weather: {weather["temp_c"]}°C, '
            f'{weather["condition"]["text"]}'
        )
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
