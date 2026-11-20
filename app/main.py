import os
import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
LANGUAGE = "pt"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("A variável API_KEY não foi configurada.")
    params = {
        "key": api_key,
        "q": CITY,
        "lang": LANGUAGE,
    }
    response = requests.get(URL, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()
    print("Cidade:", data["location"]["name"])
    print("País:", data["location"]["country"])
    print("Temperatura:", data["current"]["temp_c"], "°C")
    print("Sensação térmica:", data["current"]["feelslike_c"], "°C")
    print("Condição:", data["current"]["condition"]["text"])
    print("Umidade:", data["current"]["humidity"], "%")


if __name__ == "__main__":
    get_weather()
