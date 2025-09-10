import os
import requests

LINK = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    key = os.getenv("API_KEY")
    if not key:
        raise ValueError("Key not found")

    url = f"{LINK}?key={key}&q={CITY}"
    response = requests.get(url, timeout=5)
    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}/{country} {time}"
          f" " f"Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
